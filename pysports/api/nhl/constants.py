PARSING_SCHEME = {
    "name": "a",
    "average_age": 'td[data-stat="average_age"]:first',
    "games_played": 'td[data-stat="games"]:first',
    "wins": 'td[data-stat="wins"]:first',
    "losses": 'td[data-stat="losses"]:first',
    "overtime_losses": 'td[data-stat="losses_ot"]:first',
    "points": 'td[data-stat="points"]:first',
    "points_percentage": 'td[data-stat="points_pct"]:first',
    "goals_for": 'td[data-stat="goals"]:first',
    "goals_against": 'td[data-stat="opp_goals"]:first',
    "simple_rating_system": 'td[data-stat="srs"]:first',
    "strength_of_schedule": 'td[data-stat="sos"]:first',
    "total_goals_per_game": 'td[data-stat="total_goals_per_game"]:first',
    "power_play_goals": 'td[data-stat="goals_pp"]:first',
    "power_play_opportunities": 'td[data-stat="chances_pp"]:first',
    "power_play_percentage": 'td[data-stat="power_play_pct"]:first',
    "power_play_goals_against": 'td[data-stat="opp_goals_pp"]:first',
    "power_play_opportunities_against": 'td[data-stat="opp_chances_pp"]:first',
    "penalty_killing_percentage": 'td[data-stat="pen_kill_pct"]:first',
    "short_handed_goals": 'td[data-stat="goals_sh"]:first',
    "short_handed_goals_against": 'td[data-stat="opp_goals_sh"]:first',
    "shots_on_goal": 'td[data-stat="shots"]:first',
    "shooting_percentage": 'td[data-stat="shot_pct"]:first',
    "shots_against": 'td[data-stat="shots_against"]:first',
    "save_percentage": 'td[data-stat="save_pct"]:first',
    "pdo_at_even_strength": 'td[data-stat="pdo"]:first',
}

SCHEDULE_SCHEME = {
    "game": 'th[data-stat="games"]:first',
    "date": 'td[data-stat="date_game"]:first',
    "time": 'td[data-stat="time_game"]:first',
    "location": 'td[data-stat="game_location"]:first',
    "opponent_abbr": 'td[data-stat="opp_name"]:first',
    "opponent_name": 'td[data-stat="opp_name"]:first',
    "goals_scored": 'td[data-stat="goals"]:first',
    "goals_allowed": 'td[data-stat="opp_goals"]:first',
    "result": 'td[data-stat="game_outcome"]:first',
    "overtime": 'td[data-stat="overtimes"]:first',
    "shots_on_goal": 'td[data-stat="shots"]:first',
    "penalties_in_minutes": 'td[data-stat="pen_min"]:first',
    "power_play_goals": 'td[data-stat="goals_pp"]:first',
    "power_play_opportunities": 'td[data-stat="chances_pp"]:first',
    "short_handed_goals": 'td[data-stat="goals_sh"]:first',
    "opp_shots_on_goal": 'td[data-stat="shots_against"]:first',
    "opp_penalties_in_minutes": 'td[data-stat="pen_min_opp"]:first',
    "opp_power_play_goals": 'td[data-stat="goals_against_pp"]:first',
    "opp_power_play_opportunities": 'td[data-stat="opp_chances_pp"]:first',
    "opp_short_handed_goals": 'td[data-stat="goals_against_sh"]:first',
    "corsi_for": 'td[data-stat="corsi_for"]:first',
    "corsi_against": 'td[data-stat="corsi_against"]:first',
    "corsi_for_percentage": 'td[data-stat="corsi_pct"]:first',
    "fenwick_for": 'td[data-stat="fenwick_for"]:first',
    "fenwick_against": 'td[data-stat="fenwick_against"]:first',
    "fenwick_for_percentage": 'td[data-stat="fenwick_pct"]:first',
    "faceoff_wins": 'td[data-stat="faceoff_wins"]:first',
    "faceoff_losses": 'td[data-stat="faceoff_losses"]:first',
    "faceoff_win_percentage": 'td[data-stat="faceoff_percentage"]:first',
    "offensive_zone_start_percentage": 'td[data-stat="zs_offense_pct"]:first',
    "pdo": 'td[data-stat="pdo"]:first',
}

BOXSCORE_SCHEME = {
    "game_info": 'div[class="scorebox_meta"]',
    "away_name": 'a[itemprop="name"]:first',
    "home_name": 'a[itemprop="name"]:last',
    "away_skaters": 'table[class="sortable stats_table"]:first tbody tr',
    "away_goalies": 'table[class="sortable stats_table"]',
    "away_goals": 'tfoot td[data-stat="goals"]',
    "away_assists": 'tfoot td[data-stat="assists"]',
    "away_points": 'tfoot td[data-stat="points"]',
    "away_penalties_in_minutes": 'tfoot td[data-stat="pen_min"]',
    "away_even_strength_goals": 'tfoot td[data-stat="goals_ev"]',
    "away_power_play_goals": 'tfoot td[data-stat="goals_pp"]',
    "away_short_handed_goals": 'tfoot td[data-stat="goals_sh"]',
    "away_game_winning_goals": 'td[data-stat="goals_gw"]',
    "away_even_strength_assists": 'td[data-stat="assists_ev"]',
    "away_power_play_assists": 'td[data-stat="assists_pp"]',
    "away_short_handed_assists": 'td[data-stat="assists_sh"]',
    "away_shots_on_goal": 'tfoot td[data-stat="shots"]',
    "away_shooting_percentage": 'tfoot td[data-stat="shot_pct"]',
    "away_saves": 'td[data-stat="saves"]',
    "away_save_percentage": 'td[data-stat="save_pct"]',
    "away_shutout": 'td[data-stat="shutouts"]',
    "home_goals": 'tfoot td[data-stat="goals"]',
    "home_assists": 'tfoot td[data-stat="assists"]',
    "home_points": 'tfoot td[data-stat="points"]',
    "home_penalties_in_minutes": 'tfoot td[data-stat="pen_min"]',
    "home_even_strength_goals": 'tfoot td[data-stat="goals_ev"]',
    "home_power_play_goals": 'tfoot td[data-stat="goals_pp"]',
    "home_short_handed_goals": 'tfoot td[data-stat="goals_sh"]',
    "home_game_winning_goals": 'td[data-stat="goals_gw"]',
    "home_even_strength_assists": 'td[data-stat="assists_ev"]',
    "home_power_play_assists": 'td[data-stat="assists_pp"]',
    "home_short_handed_assists": 'td[data-stat="assists_sh"]',
    "home_shots_on_goal": 'tfoot td[data-stat="shots"]',
    "home_shooting_percentage": 'tfoot td[data-stat="shot_pct"]',
    "home_saves": 'td[data-stat="saves"]',
    "home_save_percentage": 'td[data-stat="save_pct"]',
    "home_shutout": 'td[data-stat="shutouts"]',
}

BOXSCORE_ELEMENT_INDEX = {
    "date": 0,
    "time": 0,
    "attendance": 1,
    "arena": 2,
    "duration": 3,
    "home_goals": 1,
    "home_assists": 1,
    "home_points": 1,
    "home_penalties_in_minutes": 1,
    "home_even_strength_goals": 1,
    "home_power_play_goals": 1,
    "home_short_handed_goals": 1,
    "home_shots_on_goal": 1,
    "home_shooting_percentage": 1,
    "home_saves": 1,
    "home_save_percentage": 1,
    "home_shutout": 1,
}

PLAYER_SCHEME = {
    "summary": '[data-template="Partials/Teams/Summary"]',
    "season": 'th[data-stat="season"]',
    "name": 'h1[itemprop="name"]',
    "team_abbreviation": 'td[data-stat="team_id"]',
    "height": 'span[itemprop="height"]',
    "weight": 'span[itemprop="weight"]',
    "age": 'td[data-stat="age"]',
    "league": 'td[data-stat="lg_id"]',
    "games_played": 'td[data-stat="games_played"]',
    "goals": 'td[data-stat="goals"]',
    "assists": 'td[data-stat="assists"]',
    "points": 'td[data-stat="points"]',
    "plus_minus": 'td[data-stat="plus_minus"]',
    "penalties_in_minutes": 'td[data-stat="pen_min"]',
    "even_strength_goals": 'td[data-stat="goals_ev"]',
    "power_play_goals": 'td[data-stat="goals_pp"]',
    "short_handed_goals": 'td[data-stat="goals_sh"]',
    "game_winning_goals": 'td[data-stat="goals_gw"]',
    "even_strength_assists": 'td[data-stat="assists_ev"]',
    "power_play_assists": 'td[data-stat="assists_pp"]',
    "short_handed_assists": 'td[data-stat="assists_sh"]',
    "shots_on_goal": 'td[data-stat="shots"]',
    "shooting_percentage": 'td[data-stat="shot_pct"]',
    "total_shots": 'td[data-stat="shots_attempted"]',
    "time_on_ice": 'td[data-stat="time_on_ice"]',
    "average_time_on_ice": 'td[data-stat="time_on_ice_avg"]',
    "faceoff_wins": 'td[data-stat="faceoff_wins"]',
    "faceoff_losses": 'td[data-stat="faceoff_losses"]',
    "faceoff_percentage": 'td[data-stat="faceoff_percentage"]',
    "blocks_at_even_strength": 'td[data-stat="blocks"]',
    "hits_at_even_strength": 'td[data-stat="hits"]',
    "takeaways": 'td[data-stat="takeaways"]',
    "giveaways": 'td[data-stat="giveaways"]',
    "time_on_ice_even_strength": 'td[data-stat="toi_pbp"]',
    "corsi_for": 'td[data-stat="corsi_for"]',
    "corsi_against": 'td[data-stat="corsi_against"]',
    "corsi_for_percentage": 'td[data-stat="corsi_pct"]',
    "relative_corsi_for_percentage": 'td[data-stat="corsi_rel_pct"]',
    "fenwick_for": 'td[data-stat="fenwick_for"]',
    "fenwick_against": 'td[data-stat="fenwick_against"]',
    "fenwick_for_percentage": 'td[data-stat="fenwick_pct"]',
    "relative_fenwick_for_percentage": 'td[data-stat="fenwick_rel_pct"]',
    "goals_for_on_ice": 'td[data-stat="on_goals"]',
    "shooting_percentage_on_ice": 'td[data-stat="on_ice_shot_pct"]',
    "goals_against_on_ice": 'td[data-stat="on_goals_against"]',
    "save_percentage_on_ice": 'td[data-stat="on_ice_sv_pct"]',
    "pdo": 'td[data-stat="pdo"]',
    "offensive_zone_start_percentage": 'td[data-stat="zs_offense_pct"]',
    "defensive_zone_start_percentage": 'td[data-stat="zs_defense_pct"]',
    "goals_created": 'td[data-stat="goals_created"]',
    "adjusted_goals": 'td[data-stat="goals_adjusted"]',
    "adjusted_assists": 'td[data-stat="assists_adjusted"]',
    "adjusted_points": 'td[data-stat="points_adjusted"]',
    "adjusted_goals_created": 'td[data-stat="goals_created_adjusted"]',
    "total_goals_for_on_ice": 'td[data-stat="total_goals_for"]',
    "power_play_goals_for_on_ice": 'td[data-stat="power_play_goals_for"]',
    "total_goals_against_on_ice": 'td[data-stat="total_goals_against"]',
    "power_play_goals_against_on_ice": 'td[data-stat="power_play_goals_against"]',
    "offensive_point_shares": 'td[data-stat="ops"]',
    "defensive_point_shares": 'td[data-stat="dps"]',
    "point_shares": 'td[data-stat="ps"]',
    "shootout_attempts": 'td[data-stat="so_att"]',
    "shootout_goals": 'td[data-stat="so_made"]',
    "shootout_misses": 'td[data-stat="so_miss"]',
    "shootout_percentage": 'td[data-stat="so_made_pct"]',
    "wins": 'td[data-stat="wins_goalie"]',
    "losses": 'td[data-stat="losses_goalie"]',
    "ties_plus_overtime_loss": 'td[data-stat="ties_goalie"]',
    "goals_against": 'td[data-stat="goals_against"]',
    "shots_against": 'td[data-stat="shots_against"]',
    "saves": 'td[data-stat="saves"]',
    "save_percentage": 'td[data-stat="save_pct"]',
    "goals_against_average": 'td[data-stat="goals_against_avg"]',
    "shutouts": 'td[data-stat="shutouts"]',
    "minutes": 'td[data-stat="min_goalie"]',
    "quality_starts": 'td[data-stat="quality_starts_goalie"]',
    "quality_start_percentage": 'td[data-stat="quality_start_goalie_pct"]',
    "really_bad_starts": 'td[data-stat="really_bad_starts_goalie"]',
    "goal_against_percentage_relative": 'td[data-stat="ga_pct_minus"]',
    "goals_saved_above_average": 'td[data-stat="gs_above_avg"]',
    "adjusted_goals_against_average": 'td[data-stat="goals_against_avg_adjusted"]',
    "goalie_point_shares": 'td[data-stat="gps"]',
    "even_strength_shots_faced": 'td[data-stat="shots_against_ev"]',
    "even_strength_goals_allowed": 'td[data-stat="goals_against_ev"]',
    "even_strength_save_percentage": 'td[data-stat="svpct_ev"]',
    "power_play_shots_faced": 'td[data-stat="shots_against_pp"]',
    "power_play_goals_allowed": 'td[data-stat="goals_against_pp"]',
    "power_play_save_percentage": 'td[data-stat="svpct_pp"]',
    "short_handed_shots_faced": 'td[data-stat="shots_against_sh"]',
    "short_handed_goals_allowed": 'td[data-stat="goals_against_sh"]',
    "short_handed_save_percentage": 'td[data-stat="svpct_sh"]',
    "decision": 'td[data-stat="decision"]',
    "defensive_zone_starts": 'td[data-stat="zs_def"]',
    "individual_corsi_for_events": 'td[data-stat="Cevents"]',
    "offensive_zone_starts": 'td[data-stat="zs_off"]',
    "on_ice_shot_attempts_against": 'td[data-stat="on_opp_Cevents"]',
    "on_ice_shot_attempts_for": 'td[data-stat="on_Cevents"]',
    "shifts": 'td[data-stat="shifts"]',
}

BOXSCORE_RETRY = {
    "corsi_for_percentage": 'td[data-stat="corsi_for"]',
    "offensive_zone_start_percentage": 'td[data-stat="ozs_pct"]',
    "relative_corsi_for_percentage": 'td[data-stat="corsi_rel"]',
}

SEASON_PAGE_URL = "http://www.hockey-reference.com/leagues/NHL_%s.html"

SCHEDULE_URL = "https://www.hockey-reference.com/teams/%s/%s_gamelog.html"

BOXSCORE_URL = "https://www.hockey-reference.com/boxscores/%s.html"

BOXSCORES_URL = (
    "https://www.hockey-reference.com/boxscores/index.fcgi?" "month=%s&day=%s&year=%s"
)
PLAYER_URL = "https://www.hockey-reference.com/players/%s/%s.html"
ROSTER_URL = "https://www.hockey-reference.com/teams/%s/%s.html"

SHOOTOUT = -1
OVERTIME_LOSS = "OTL"