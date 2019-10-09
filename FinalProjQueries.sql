#Combo guard
SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `FG%` > .38 AND `FG%` < .42 AND `TOV` < 1 AND `USG%` > 10 GROUP BY player_name ORDER BY num_of_seasons DESC;

CREATE OR REPLACE VIEW combo_guard AS SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `FG%` > .38 AND `FG%` < .42 AND `TOV` < 1 AND `USG%` > 10 GROUP BY player_name ORDER BY num_of_seasons DESC;

#Floor general
SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `AST%` > 20 AND `TOV%` < 10 AND `USG%` > 10 AND WS >8 GROUP BY player_name ORDER BY num_of_seasons DESC;

CREATE OR REPLACE VIEW floor_general AS SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `AST%` > 20 AND `TOV%` < 10 AND `USG%` > 10 AND WS >8 GROUP BY player_name ORDER BY num_of_seasons DESC;

#Shooting Wing
SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `3PAst'd%` > .3 AND `16 <3ft FG%` > .2 AND `3Pft FG%` > .3 AND `TS%` > .6 GROUP BY player_name ORDER BY num_of_seasons DESC;

CREATE OR REPLACE VIEW shooting_wing AS SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `3PAst'd%` > .3 AND `16 <3ft FG%` > .2 AND `3Pft FG%` > .3 AND `TS%` > .6 GROUP BY player_name ORDER BY num_of_seasons DESC;

#Scoring Wing
SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `3PAst'd%` > .3 AND FTr > .2 AND `TS%` > .6 GROUP BY player_name ORDER BY num_of_seasons DESC;

CREATE OR REPLACE VIEW scoring_wing AS SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `3PAst'd%` > .3 AND FTr > .2 AND `TS%` > .6 GROUP BY player_name ORDER BY num_of_seasons DESC;

#3&D Wing
SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `3PA%` > .4 AND DRtg > 110 AND `3Pft FG%` > .4 GROUP BY player_name ORDER BY num_of_seasons DESC;

CREATE OR REPLACE VIEW 3d_wing AS SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `3PA%` > .4 AND DRtg > 110 AND `3Pft FG%` > .4 GROUP BY player_name ORDER BY num_of_seasons DESC;

#Offensive Center
SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `FT%` > .8 AND ORB > 4 AND FTr > .2 AND `0-3ft FA%` > .3 GROUP BY player_name ORDER BY num_of_seasons DESC;

CREATE OR REPLACE VIEW offensive_center AS SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `FT%` > .8 AND ORB > 4 AND FTr > .2 AND `0-3ft FA%` > .3 GROUP BY player_name ORDER BY num_of_seasons DESC;

#Defensive Center
SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `DRB%` > 12 AND DRB > 6 AND DRtg > 110 AND `BLK%` > .6 GROUP BY player_name ORDER BY num_of_seasons DESC;

CREATE OR REPLACE VIEW defensive_center AS SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `DRB%` > 12 AND DRB > 6 AND DRtg > 110 AND `BLK%` > .6 GROUP BY player_name ORDER BY num_of_seasons DESC;

#Versatile Forward
SELECT player_name FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `FT%` > .8 AND `Dist.` > 10 AND `Dist.` < 14 AND `TS%` > .6;

SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `FT%` > .8 AND `Dist.` > 10 AND `Dist.` < 14 AND `TS%` > .6 GROUP BY player_name ORDER BY num_of_seasons DESC;

CREATE OR REPLACE VIEW versatile_forward AS SELECT player_name, COUNT(*) num_of_seasons FROM player_index NATURAL JOIN per100_stats NATURAL JOIN adv_stats NATURAL JOIN shooting_stats WHERE `FT%` > .8 AND `Dist.` > 10 AND `Dist.` < 14 AND `TS%` > .6 GROUP BY player_name ORDER BY num_of_seasons DESC;
