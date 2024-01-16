PARSING_SCHEME = {
    "name": "a",
    "games_played": 'td[data-stat="g"]:first',
    "wins": 'td[data-stat="wins"]:first',
    "losses": 'td[data-stat="losses"]:first',
    "win_percentage": 'td[data-stat="win_loss_pct"]:first',
    "simple_rating_system": 'td[data-stat="srs"]:first',
    "strength_of_schedule": 'td[data-stat="sos"]:first',
    "conference_wins": 'td[data-stat="wins_conf"]:first',
    "conference_losses": 'td[data-stat="losses_conf"]:first',
    "home_wins": 'td[data-stat="wins_home"]:first',
    "home_losses": 'td[data-stat="losses_home"]:first',
    "away_wins": 'td[data-stat="wins_visitor"]:first',
    "away_losses": 'td[data-stat="losses_visitor"]:first',
    "points": 'td[data-stat="pts"]:first',
    "opp_points": 'td[data-stat="opp_pts"]:first',
    "minutes_played": 'td[data-stat="mp"]:first',
    "field_goals": 'td[data-stat="fg"]:first',
    "field_goal_attempts": 'td[data-stat="fga"]:first',
    "field_goal_percentage": 'td[data-stat="fg_pct"]:first',
    "three_point_field_goals": 'td[data-stat="fg3"]:first',
    "three_point_field_goal_attempts": 'td[data-stat="fg3a"]:first',
    "three_point_field_goal_percentage": 'td[data-stat="fg3_pct"]:first',
    "two_point_field_goals": 'td[data-stat="fg2"]:first',
    "two_point_field_goal_attempts": 'td[data-stat="fg2a"]:first',
    "two_point_field_goal_percentage": 'td[data-stat="fg2_pct"]:first',
    "free_throws": 'td[data-stat="ft"]:first',
    "free_throw_attempts": 'td[data-stat="fta"]:first',
    "free_throw_percentage": 'td[data-stat="ft_pct"]:first',
    "offensive_rebounds": 'td[data-stat="orb"]:first',
    "defensive_rebounds": 'td[data-stat="drb"]:first',
    "total_rebounds": 'td[data-stat="trb"]:first',
    "assists": 'td[data-stat="ast"]:first',
    "steals": 'td[data-stat="stl"]:first',
    "blocks": 'td[data-stat="blk"]:first',
    "turnovers": 'td[data-stat="tov"]:first',
    "personal_fouls": 'td[data-stat="pf"]:first',
    "points": 'td[data-stat="pts"]:first',
    "opp_minutes_played": 'td[data-stat="opp_mp"]:first',
    "opp_field_goals": 'td[data-stat="opp_fg"]:first',
    "opp_field_goal_attempts": 'td[data-stat="opp_fga"]:first',
    "opp_field_goal_percentage": 'td[data-stat="opp_fg_pct"]:first',
    "opp_three_point_field_goals": 'td[data-stat="opp_fg3"]:first',
    "opp_three_point_field_goal_attempts": 'td[data-stat="opp_fg3a"]:first',
    "opp_three_point_field_goal_percentage": 'td[data-stat="opp_fg3_pct"]:first',
    "opp_two_point_field_goals": 'td[data-stat="opp_fg2"]:first',
    "opp_two_point_field_goal_attempts": 'td[data-stat="opp_fg2a"]:first',
    "opp_two_point_field_goal_percentage": 'td[data-stat="opp_fg2_pct"]:first',
    "opp_free_throws": 'td[data-stat="opp_ft"]:first',
    "opp_free_throw_attempts": 'td[data-stat="opp_fta"]:first',
    "opp_free_throw_percentage": 'td[data-stat="opp_ft_pct"]:first',
    "opp_offensive_rebounds": 'td[data-stat="opp_orb"]:first',
    "opp_defensive_rebounds": 'td[data-stat="opp_drb"]:first',
    "opp_total_rebounds": 'td[data-stat="opp_trb"]:first',
    "opp_assists": 'td[data-stat="opp_ast"]:first',
    "opp_steals": 'td[data-stat="opp_stl"]:first',
    "opp_blocks": 'td[data-stat="opp_blk"]:first',
    "opp_turnovers": 'td[data-stat="opp_tov"]:first',
    "opp_personal_fouls": 'td[data-stat="opp_pf"]:first',
    "opp_points": 'td[data-stat="opp_pts"]:first',
    "pace": 'td[data-stat="pace"]:first',
    "offensive_rating": 'td[data-stat="off_rtg"]:first',
    "free_throw_attempt_rate": 'td[data-stat="fta_per_fga_pct"]:first',
    "three_point_attempt_rate": 'td[data-stat="fg3a_per_fga_pct"]:first',
    "true_shooting_percentage": 'td[data-stat="ts_pct"]:first',
    "total_rebound_percentage": 'td[data-stat="trb_pct"]:first',
    "assist_percentage": 'td[data-stat="ast_pct"]:first',
    "steal_percentage": 'td[data-stat="stl_pct"]:first',
    "block_percentage": 'td[data-stat="blk_pct"]:first',
    "effective_field_goal_percentage": 'td[data-stat="efg_pct"]:first',
    "turnover_percentage": 'td[data-stat="tov_pct"]:first',
    "offensive_rebound_percentage": 'td[data-stat="orb_pct"]:first',
    "free_throws_per_field_goal_attempt": 'td[data-stat="ft_rate"]:first',
    "opp_offensive_rating": 'td[data-stat="def_rtg"]:first',
    "opp_free_throw_attempt_rate": 'td[data-stat="opp_fta_per_fga_pct"]:first',
    "opp_three_point_attempt_rate": 'td[data-stat="opp_fg3a_per_fga_pct"]:first',
    "opp_true_shooting_percentage": 'td[data-stat="opp_ts_pct"]:first',
    "opp_total_rebound_percentage": 'td[data-stat="opp_trb_pct"]:first',
    "opp_assist_percentage": 'td[data-stat="opp_ast_pct"]:first',
    "opp_steal_percentage": 'td[data-stat="opp_stl_pct"]:first',
    "opp_block_percentage": 'td[data-stat="opp_blk_pct"]:first',
    "opp_effective_field_goal_percentage": 'td[data-stat="opp_efg_pct"]:first',
    "opp_turnover_percentage": 'td[data-stat="opp_tov_pct"]:first',
    "opp_offensive_rebound_percentage": 'td[data-stat="opp_orb_pct"]:first',
    "opp_free_throws_per_field_goal_attempt": 'td[data-stat="opp_ft_rate"]:first',
}

SCHEDULE_SCHEME = {
    "game": 'th[data-stat="g"]:first',
    "date": 'td[data-stat="date_game"]:first',
    "time": 'td[data-stat="time_game"]:first',
    "type": 'td[data-stat="game_type"]:first',
    "location": 'td[data-stat="game_location"]:first',
    "opponent_abbr": 'td[data-stat="opp_name"]:first',
    "opponent_name": 'td[data-stat="opp_name"]:first',
    "opponent_conference": 'td[data-stat="conf_abbr"]:first',
    "result": 'td[data-stat="game_result"]:first',
    "points_for": 'td[data-stat="pts"]:first',
    "points_against": 'td[data-stat="opp_pts"]:first',
    "overtimes": 'td[data-stat="overtimes"]:first',
    "season_wins": 'td[data-stat="wins"]:first',
    "season_losses": 'td[data-stat="losses"]:first',
    "streak": 'td[data-stat="game_streak"]:first',
    "arena": 'td[data-stat="arena"]:first',
}

BOXSCORE_SCHEME = {
    "date": 'div[class="scorebox_meta"]',
    "location": 'div[class="scorebox_meta"]',
    "away_name": 'a[itemprop="name"]:first',
    "home_name": 'a[itemprop="name"]:last',
    "winning_name": "",
    "winning_abbr": "",
    "losing_name": "",
    "losing_abbr": "",
    "summary": "table#line-score",
    "pace": 'td[data-stat="pace"]:first',
    "away_record": 'div#boxes div[class="section_heading"] h2',
    "away_minutes_played": 'tfoot td[data-stat="mp"]',
    "away_field_goals": 'tfoot td[data-stat="fg"]',
    "away_field_goal_attempts": 'tfoot td[data-stat="fga"]',
    "away_field_goal_percentage": 'tfoot td[data-stat="fg_pct"]',
    "away_two_point_field_goals": 'tfoot td[data-stat="fg2"]',
    "away_two_point_field_goal_attempts": 'tfoot td[data-stat="fg2a"]',
    "away_two_point_field_goal_percentage": 'tfoot td[data-stat="fg2_pct"]',
    "away_three_point_field_goals": 'tfoot td[data-stat="fg3"]',
    "away_three_point_field_goal_attempts": 'tfoot td[data-stat="fg3a"]',
    "away_three_point_field_goal_percentage": 'tfoot td[data-stat="fg3_pct"]',
    "away_free_throws": 'tfoot td[data-stat="ft"]',
    "away_free_throw_attempts": 'tfoot td[data-stat="fta"]',
    "away_free_throw_percentage": 'tfoot td[data-stat="ft_pct"]',
    "away_offensive_rebounds": 'tfoot td[data-stat="orb"]',
    "away_defensive_rebounds": 'tfoot td[data-stat="drb"]',
    "away_total_rebounds": 'tfoot td[data-stat="trb"]',
    "away_assists": 'tfoot td[data-stat="ast"]',
    "away_steals": 'tfoot td[data-stat="stl"]',
    "away_blocks": 'tfoot td[data-stat="blk"]',
    "away_turnovers": 'tfoot td[data-stat="tov"]',
    "away_personal_fouls": 'tfoot td[data-stat="pf"]',
    "away_points": 'tfoot td[data-stat="pts"]',
    "away_true_shooting_percentage": 'tfoot td[data-stat="ts_pct"]',
    "away_effective_field_goal_percentage": 'tfoot td[data-stat="efg_pct"]',
    "away_three_point_attempt_rate": 'tfoot td[data-stat="fg3a_per_fga_pct"]',
    "away_free_throw_attempt_rate": 'tfoot td[data-stat="fta_per_fga_pct"]',
    "away_offensive_rebound_percentage": 'tfoot td[data-stat="orb_pct"]',
    "away_defensive_rebound_percentage": 'tfoot td[data-stat="drb_pct"]',
    "away_total_rebound_percentage": 'tfoot td[data-stat="trb_pct"]',
    "away_assist_percentage": 'tfoot td[data-stat="ast_pct"]',
    "away_steal_percentage": 'tfoot td[data-stat="stl_pct"]',
    "away_block_percentage": 'tfoot td[data-stat="blk_pct"]',
    "away_turnover_percentage": 'tfoot td[data-stat="tov_pct"]',
    "away_offensive_rating": 'tfoot td[data-stat="off_rtg"]',
    "away_defensive_rating": 'tfoot td[data-stat="def_rtg"]',
    "away_ranking": 'div[class="game_summary nohover current"] tr',
    "home_record": 'div#boxes div[class="section_heading"] h2',
    "home_minutes_played": 'tfoot td[data-stat="mp"]',
    "home_field_goals": 'tfoot td[data-stat="fg"]',
    "home_field_goal_attempts": 'tfoot td[data-stat="fga"]',
    "home_field_goal_percentage": 'tfoot td[data-stat="fg_pct"]',
    "home_two_point_field_goals": 'tfoot td[data-stat="fg2"]',
    "home_two_point_field_goal_attempts": 'tfoot td[data-stat="fg2a"]',
    "home_two_point_field_goal_percentage": 'tfoot td[data-stat="fg2_pct"]',
    "home_three_point_field_goals": 'tfoot td[data-stat="fg3"]',
    "home_three_point_field_goal_attempts": 'tfoot td[data-stat="fg3a"]',
    "home_three_point_field_goal_percentage": 'tfoot td[data-stat="fg3_pct"]',
    "home_free_throws": 'tfoot td[data-stat="ft"]',
    "home_free_throw_attempts": 'tfoot td[data-stat="fta"]',
    "home_free_throw_percentage": 'tfoot td[data-stat="ft_pct"]',
    "home_offensive_rebounds": 'tfoot td[data-stat="orb"]',
    "home_defensive_rebounds": 'tfoot td[data-stat="drb"]',
    "home_total_rebounds": 'tfoot td[data-stat="trb"]',
    "home_assists": 'tfoot td[data-stat="ast"]',
    "home_steals": 'tfoot td[data-stat="stl"]',
    "home_blocks": 'tfoot td[data-stat="blk"]',
    "home_turnovers": 'tfoot td[data-stat="tov"]',
    "home_personal_fouls": 'tfoot td[data-stat="pf"]',
    "home_points": 'tfoot td[data-stat="pts"]',
    "home_true_shooting_percentage": 'tfoot td[data-stat="ts_pct"]',
    "home_effective_field_goal_percentage": 'tfoot td[data-stat="efg_pct"]',
    "home_three_point_attempt_rate": 'tfoot td[data-stat="fg3a_per_fga_pct"]',
    "home_free_throw_attempt_rate": 'tfoot td[data-stat="fta_per_fga_pct"]',
    "home_offensive_rebound_percentage": 'tfoot td[data-stat="orb_pct"]',
    "home_defensive_rebound_percentage": 'tfoot td[data-stat="drb_pct"]',
    "home_total_rebound_percentage": 'tfoot td[data-stat="trb_pct"]',
    "home_assist_percentage": 'tfoot td[data-stat="ast_pct"]',
    "home_steal_percentage": 'tfoot td[data-stat="stl_pct"]',
    "home_block_percentage": 'tfoot td[data-stat="blk_pct"]',
    "home_turnover_percentage": 'tfoot td[data-stat="tov_pct"]',
    "home_offensive_rating": 'tfoot td[data-stat="off_rtg"]',
    "home_defensive_rating": 'tfoot td[data-stat="def_rtg"]',
    "home_ranking": 'div[class="game_summary nohover current"] tr',
}

BOXSCORE_ELEMENT_INDEX = {
    "date": 0,
    "location": 1,
    "away_ranking": 0,
    "home_ranking": 1,
    "home_record": 1,
    "home_minutes_played": 1,
    "home_field_goals": 1,
    "home_field_goal_attempts": 1,
    "home_field_goal_percentage": 1,
    "home_two_point_field_goals": 1,
    "home_two_point_field_goal_attempts": 1,
    "home_two_point_field_goal_percentage": 1,
    "home_three_point_field_goals": 1,
    "home_three_point_field_goal_attempts": 1,
    "home_three_point_field_goal_percentage": 1,
    "home_free_throws": 1,
    "home_free_throw_attempts": 1,
    "home_free_throw_percentage": 1,
    "home_offensive_rebounds": 1,
    "home_defensive_rebounds": 1,
    "home_total_rebounds": 1,
    "home_assists": 1,
    "home_steals": 1,
    "home_blocks": 1,
    "home_turnovers": 1,
    "home_personal_fouls": 1,
    "home_points": 1,
    "home_true_shooting_percentage": 1,
    "home_effective_field_goal_percentage": 1,
    "home_three_point_attempt_rate": 1,
    "home_free_throw_attempt_rate": 1,
    "home_offensive_rebound_percentage": 1,
    "home_defensive_rebound_percentage": 1,
    "home_total_rebound_percentage": 1,
    "home_assist_percentage": 1,
    "home_steal_percentage": 1,
    "home_block_percentage": 1,
    "home_turnover_percentage": 1,
    "home_offensive_rating": 1,
    "home_defensive_rating": 1,
}

RANKINGS_SCHEME = {
    "name": 'td[data-stat="school_name"]',
    "week": 'th[data-stat="week_poll"]',
    "date": 'td[data-stat="date_poll"]',
    "rank": 'td[data-stat="rank"]',
    "previous": 'td[data-stat="rank_prev"]',
    "change": 'td[data-stat="rank_diff"]',
}

PLAYER_SCHEME = {
    "summary": '[data-template="Partials/Teams/Summary"]',
    "conference": 'td[data-stat="conf_abbr"]',
    "season": 'th[data-stat="season"]:first',
    "name": "h1",
    "team_abbreviation": 'td[data-stat="school_name"]',
    "position": 'td[data-stat="pos"]',
    "height": 'span[itemprop="height"]',
    "weight": 'span[itemprop="weight"]',
    "birth_date": 'td[data-stat=""]',
    "nationality": 'td[data-stat=""]',
    "age": "nobr",
    "games_played": 'td[data-stat="g"]',
    "games_started": 'td[data-stat="gs"]',
    "minutes_played": 'td[data-stat="mp"]',
    "field_goals": 'td[data-stat="fg"]',
    "field_goal_attempts": 'td[data-stat="fga"]',
    "field_goal_percentage": 'td[data-stat="fg_pct"]',
    "three_pointers": 'td[data-stat="fg3"]',
    "three_point_attempts": 'td[data-stat="fg3a"]',
    "three_point_percentage": 'td[data-stat="fg3_pct"]',
    "two_pointers": 'td[data-stat="fg2"]',
    "two_point_attempts": 'td[data-stat="fg2a"]',
    "two_point_percentage": 'td[data-stat="fg2_pct"]',
    "effective_field_goal_percentage": 'td[data-stat="efg_pct"]',
    "free_throws": 'td[data-stat="ft"]',
    "free_throw_attempts": 'td[data-stat="fta"]',
    "free_throw_percentage": 'td[data-stat="ft_pct"]',
    "offensive_rebounds": 'td[data-stat="orb"]',
    "defensive_rebounds": 'td[data-stat="drb"]',
    "total_rebounds": 'td[data-stat="trb"]',
    "assists": 'td[data-stat="ast"]',
    "steals": 'td[data-stat="stl"]',
    "blocks": 'td[data-stat="blk"]',
    "turnovers": 'td[data-stat="tov"]',
    "personal_fouls": 'td[data-stat="pf"]',
    "points": 'td[data-stat="pts"]',
    "player_efficiency_rating": 'td[data-stat="per"]',
    "true_shooting_percentage": 'td[data-stat="ts_pct"]',
    "three_point_attempt_rate": 'td[data-stat="fg3a_per_fga_pct"]',
    "free_throw_attempt_rate": 'td[data-stat="fta_per_fga_pct"]',
    "points_produced": 'td[data-stat="pprod"]',
    "offensive_rebound_percentage": 'td[data-stat="orb_pct"]',
    "defensive_rebound_percentage": 'td[data-stat="drb_pct"]',
    "total_rebound_percentage": 'td[data-stat="trb_pct"]',
    "assist_percentage": 'td[data-stat="ast_pct"]',
    "steal_percentage": 'td[data-stat="stl_pct"]',
    "block_percentage": 'td[data-stat="blk_pct"]',
    "turnover_percentage": 'td[data-stat="tov_pct"]',
    "usage_percentage": 'td[data-stat="usg_pct"]',
    "offensive_win_shares": 'td[data-stat="ows"]',
    "defensive_win_shares": 'td[data-stat="dws"]',
    "win_shares": 'td[data-stat="ws"]',
    "win_shares_per_40_minutes": 'td[data-stat="ws_per_40"]',
    "offensive_box_plus_minus": 'td[data-stat="obpm"]',
    "defensive_box_plus_minus": 'td[data-stat="dbpm"]',
    "box_plus_minus": 'td[data-stat="bpm"]',
    "offensive_rating": 'td[data-stat="off_rtg"]',
    "defensive_rating": 'td[data-stat="def_rtg"]',
}

BASIC_STATS_URL = "https://www.sports-reference.com/cbb/seasons/" "%s-school-stats.html"
BASIC_OPPONENT_STATS_URL = (
    "https://www.sports-reference.com/cbb/seasons/" "%s-opponent-stats.html"
)
ADVANCED_STATS_URL = (
    "https://www.sports-reference.com/cbb/seasons/" "%s-advanced-school-stats.html"
)
ADVANCED_OPPONENT_STATS_URL = (
    "https://www.sports-reference.com/cbb/seasons/" "%s-advanced-opponent-stats.html"
)

SCHEDULE_URL = "https://www.sports-reference.com/cbb/schools/%s/" "%s-schedule.html"
BOXSCORE_URL = "https://www.sports-reference.com/cbb/boxscores/%s.html"
BOXSCORES_URL = (
    "https://www.sports-reference.com/cbb/boxscores/index.cgi?"
    "month=%s&day=%s&year=%s"
)
RANKINGS_URL = "https://www.sports-reference.com/cbb/seasons/%s-polls-old.html"
CONFERENCES_URL = "https://www.sports-reference.com/cbb/seasons/%s.html"
CONFERENCE_URL = "https://www.sports-reference.com/cbb/conferences/%s/%s.html"
PLAYER_URL = "https://www.sports-reference.com/cbb/players/%s.html"
ROSTER_URL = "https://www.sports-reference.com/cbb/schools/%s/%s.html"

NCAA_TOURNAMENT = "NCAA"
NIT_TOURNAMENT = "NIT"
CBI_TOURNAMENT = "CBI"
CIT_TOURNAMENT = "CIT"
