import re
import time
from datetime import datetime

import requests
from lxml.etree import ParserError, XMLSyntaxError
from pyquery import PyQuery as pq

import urllib.error
import urllib.request

from tenacity import retry, retry_if_exception, stop_after_attempt, wait_fixed
from tenacity.wait import wait_base

# {
#   league name: {
#     start month - integer referring to the month that a season typically
#                   begins. Months are 1-based, so January would be 1
#     wrap - boolean is True when a season spans multiple calendar years, such
#            as the NBA. False when a season is contained in a single calendar
#            year, such as the MLB
#   }
# }
SEASON_START_MONTH = {
    "mlb": {"start": 4, "wrap": False},
    "nba": {"start": 10, "wrap": True},
    "ncaab": {"start": 11, "wrap": True},
    "ncaaf": {"start": 8, "wrap": False},
    "nfl": {"start": 9, "wrap": False},
    "nhl": {"start": 10, "wrap": True},
}


def _date_today():
    """
    Get today's date.

    Returns the current date and time. In a standalone function to easily be
    mocked in unit tests.

    Returns
    -------
    datetime.datetime
        The current date and time as a datetime object.
    """
    return datetime.now()


class retry_if_http_429_error(retry_if_exception):
    """Retry strategy that retries if the exception is an ``HTTPError`` with
    a 429 status code.

    """

    def __init__(self):
        def is_http_429_error(exception):
            return (
                isinstance(exception, urllib.error.HTTPError)
                and exception.getcode() == 429
            )

        super().__init__(predicate=is_http_429_error)


class wait_for_retry_after_header(wait_base):
    """Wait strategy that tries to wait for the length specified by
    the Retry-After header, or the underlying wait strategy if not.
    See RFC 6585 § 4.

    Otherwise, wait according to the fallback strategy.
    """

    def __init__(self, fallback):
        self.fallback = fallback

    def __call__(self, retry_state):
        # retry_state is an instance of tenacity.RetryCallState.  The .outcome
        # property is the result/exception that came from the underlying function.
        exc = retry_state.outcome.exception()
        if isinstance(exc, urllib.error.HTTPError):
            retry_after = exc.headers.get("Retry-After")

            try:
                return int(retry_after)
            except (TypeError, ValueError):
                pass

        return self.fallback(retry_state)


@retry(
    retry=retry_if_http_429_error(),
    wait=wait_for_retry_after_header(fallback=wait_fixed(1)),
    stop=stop_after_attempt(10),
)
def _rate_limit_pq(url, sleep=3.5):
    ret = pq(url=url)
    time.sleep(sleep)
    return ret


def _url_exists(url):
    """
    Determine if a URL is valid and exists.

    Not every URL that is provided is valid and exists, such as requesting
    stats for a season that hasn't yet begun. In this case, the URL needs to be
    validated prior to continuing any code to ensure no unhandled exceptions
    occur.

    Parameters
    ----------
    url : string
        A string representation of the url to check.

    Returns
    -------
    bool
        Evaluates to True when the URL exists and is valid, otherwise returns
        False.
    """
    try:
        response = requests.head(url)
        if response.status_code == 301:
            response = requests.get(url)
            if response.status_code < 400:
                return True
            else:
                return False
        elif response.status_code < 400:
            return True
        else:
            return False
    except Exception:
        return False


def _find_year_for_season(league):
    """
    Return the necessary seasons year based on the current date.

    Since all sports start and end at different times throughout the year,
    simply using the current year is not sufficient to describe a season. For
    example, the NCAA Men's Basketball season begins in November every year.
    However, for the November and December months, the following year is used
    to denote the season (i.e. November 2017 marks the start of the '2018'
    season) on sports-reference.com. This rule does not apply to all sports.
    Baseball begins and ends in one single calendar year, so the year never
    needs to be incremented.

    Additionally, since information for future seasons is generally not
    finalized until a month before the season begins, the year will default to
    the most recent season until the month prior to the season start date. For
    example, the 2018 MLB season begins in April. In January 2018, however, not
    all season information is present in the system, so the default
    year will be '2017'.

    Parameters
    ----------
    league : string
        A string pertaining to the league start information as listed in
        SEASON_START_MONTH (i.e. 'mlb', 'nba', 'nfl', etc.). League must be
        present in SEASON_START_MONTH.

    Returns
    -------
    int
        The respective season's year.

    Raises
    ------
    ValueError
        If the passed 'league' is not a key in SEASON_START_MONTH.
    """
    today = _date_today()
    if league not in SEASON_START_MONTH:
        raise ValueError('"%s" league cannot be found!')
    start = SEASON_START_MONTH[league]["start"]
    wrap = SEASON_START_MONTH[league]["wrap"]
    if wrap and start - 1 <= today.month <= 12:
        return today.year + 1
    elif not wrap and start == 1 and today.month == 12:
        return today.year + 1
    elif not wrap and not start - 1 <= today.month <= 12:
        return today.year - 1
    else:
        return today.year


def _parse_abbreviation(uri_link):
    """
    Returns a team's abbreviation.

    A school or team's abbreviation is generally embedded in a URI link which
    contains other relative link information. For example, the URI for the
    New England Patriots for the 2017 season is "/teams/nwe/2017.htm". This
    function strips all contents before and after "nwe" and converts it
    to uppercase and returns "NWE".

    Parameters
    ----------
    uri_link : string
        A URI link which contains a team's abbreviation within other link
        contents.

    Returns
    -------
    string
        The shortened uppercase abbreviation for a given team.
    """
    abbr = re.sub(r"/[0-9]+\..*htm.*", "", uri_link("a").attr("href"))
    abbr = re.sub(r"/.*/schools/", "", abbr)
    abbr = re.sub(r"/teams/", "", abbr)
    return abbr.upper()


def _parse_field(
    parsing_scheme, html_data, field, index=0, strip=False, secondary_index=None
):
    """
    Parse an HTML table to find the requested field's value.

    All the values are passed in an HTML table row instead of as individual
    items. The values need to be parsed by matching the requested attribute
    with a parsing scheme that sports-reference uses to differentiate stats.
    This function returns a single value for the given attribute.

    Parameters
    ----------
    parsing_scheme : dict
        A dictionary of the parsing scheme to be used to find the desired
        field. The key corresponds to the attribute name to parse, and the
        value is a PyQuery-readable parsing scheme as a string (such as
        'td[data-stat="wins"]').
    html_data : string
        A string containing all the rows of stats for a given team. If
        multiple tables are being referenced, this will consist of multiple rows in a single string.
    field : string
        The name of the attribute to match. Field must be a key in
        parsing_scheme.
    index : int (optional)
        An optional index if multiple fields have the same attribute name. For
        example, 'HR' may stand for the number of home runs a baseball team has
        hit, or the number of home runs a pitcher has given up. The index
        aligns with the order in which the attributes are received in the
        html_data parameter.
    strip : boolean (optional)
        An optional boolean value which will remove any empty or invalid
        elements which might show up during list comprehensions. Specify True
        if the invalid elements should be removed from lists, which can help
        with reverse indexing.
    secondary_index : int (optional)
        An optional index if multiple fields have the same attribute, but the
        original index specified above doesn't work. This happens if a page
        doesn't have all the intended information, and the requested index
        isn't valid, causing the value to be None. Instead, a secondary index
        could be checked prior to returning None.

    Returns
    -------
    string
        The value at the specified index for the requested field. If no value
        could be found, returns None.
    """
    if field == "abbreviation":
        return _parse_abbreviation(html_data)
    scheme = parsing_scheme[field]
    if strip:
        items = [i.text() for i in html_data(scheme).items() if i.text()]
    else:
        items = [i.text() for i in html_data(scheme).items()]
    # Stats can be added and removed on a yearly basis. If not stats are found,
    # return None and have it be the value.
    if len(items) == 0:
        return None
    # Default to returning the first element. Optionally return another element
    # if multiple fields have the same tag attribute.
    try:
        return items[index]
    except IndexError:
        if secondary_index:
            try:
                return items[secondary_index]
            except IndexError:
                return None
        return None


def _remove_html_comment_tags(html):
    """
    Returns the passed HTML contents with all comment tags removed while
    keeping the contents within the tags.

    Some pages embed the HTML contents in comments. Since the HTML contents are
    valid, removing the content tags (but not the actual code within the
    comments) will return the desired contents.

    Parameters
    ----------
    html : PyQuery object
        A PyQuery object which contains the requested HTML page contents.

    Returns
    -------
    string
        The passed HTML contents with all comment tags removed.
    """
    return str(html).replace("<!--", "").replace("-->", "")


def _get_stats_table(html_page, div, footer=False):
    """
    Returns a generator of all rows in a requested table.

    When given a PyQuery HTML object and a requested div, this function creates
    a generator where every item is a PyQuery object pertaining to every row in
    the table. Generally, each row will contain multiple stats for a given
    player or team.

    Parameters
    ----------
    html_page : PyQuery object
        A PyQuery object which contains the requested HTML page contents.
    div : string
        The requested tag type and id string in the format "<tag>#<id name>"
        which aligns to the desired table in the HTML page. For example,
        "div#all_stats_table" or "table#conference_standings".
    footer : boolean (optional)
        Optionally return the table footer rows instead of the table header.

    Returns
    -------
    generator
        A generator of all row items in a given table.
    """
    stats_html = html_page(div)
    try:
        stats_table = pq(_remove_html_comment_tags(stats_html))
    except (ParserError, XMLSyntaxError):
        return None
    if footer:
        teams_list = stats_table("tfoot tr").items()
    else:
        teams_list = stats_table("tbody tr").items()
    return teams_list


def _pull_page(url=None, local_file=None):
    """
    Pull data from a local file if exists, or download data from the website.

    If local_file is passed, users can pull data directly from a local file
    which has already been downloaded instead of downloading from
    sports-reference.com using the package. This reduces server load on their
    end, and allows package users to work offline.

    Parameters
    ----------
    url : string (optional)
        A ``string`` of the URL to pull data from.
    local_file : string (optional)
        A link to a local file which has been pre-downloaded from the website.

    Returns
    -------
    PyQuery object
        Returns a ``PyQuery`` object representing the file that was either
        downloaded or read.

    Raises
    ------
    ValueError
        Raises a ``ValueError`` if neither the URL nor the local_file
        parameters were specified.
    """
    if local_file:
        with open(local_file, "r", encoding="utf8") as filehandle:
            return pq(filehandle.read())
    if url:
        return _rate_limit_pq(url=url)
    raise ValueError("Expected either a URL or a local data file!")


def check_url_validity(url):
    """
    Checks if a given URL is valid and accessible.

    Args:
    url (str): The URL to check.

    Returns:
    bool: True if the URL is valid and accessible, False otherwise.
    """
    try:
        response = requests.get(url)
        # Check if the status code is 200 (OK)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        # If any exception occurred while making the request, return False
        return False


def _no_data_found():
    """
    Print a message that no data could be found on the page.

    Occasionally, such as right before the beginning of a season, a page will
    return a valid response but will have no data beyond the default
    HTML and CSS template. With no data present on the page, pysports.api
    can't parse any information and should indicate the lack of data and return
    safely.
    """
    print(
        "The requested page returned a valid response, but no data could be "
        "found. Has the season begun, and is the data available on "
        "www.sports-reference.com?"
    )
    return
