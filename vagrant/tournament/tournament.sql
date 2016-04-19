-- Database
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- Connect to Tournament DB
\c tournament;

-- Users?

-- Tables
DROP TABLE IF EXISTS players;
CREATE TABLE players(
  player_id   SERIAL  PRIMARY KEY,
  name        TEXT    NOT NULL
);

DROP TABLE IF EXISTS matches;
CREATE TABLE matches(
  match_id    SERIAL  PRIMARY KEY,
  winner_id   INTEGER REFERENCES players (player_id),
  loser_id    INTEGER REFERENCES players (player_id)
);

-- Views
CREATE OR REPLACE VIEW player_standings AS
  SELECT p.player_id, p.name,
         (SELECT COUNT(m1.winner_id) FROM matches m1 WHERE m1.winner_id = p.player_id) wins,
         (SELECT COUNT(*) FROM matches m2 WHERE (m2.winner_id = p.player_id OR m2.loser_id = p.player_id)) matches
    FROM players p;

-- Test Data (Remove before running test script)
insert into players(name) values('Michelle');
insert into players(name) values('NinjaPanda');
insert into players(name) values('Mike');
insert into players(name) values('Salty');
insert into players(name) values('Taryn');
insert into players(name) values('Ellie');
insert into players(name) values('Braden');
insert into players(name) values('Bluesy');

insert into matches(winner_id, loser_id) values(1,2);
insert into matches(winner_id, loser_id) values(3,4);
insert into matches(winner_id, loser_id) values(5,6);
insert into matches(winner_id, loser_id) values(7,8);

select a.player_id, a.name, a.wins, b.player_id, b.name, b.wins
  from player_standings a,
   (select player_id, name, wins from player_standings) b
 where a.wins >= b.wins
   and a.player_id < b.player_id
order by a.wins desc, a.player_id, b.wins desc, b.player_id;

select a.player_id, a.name
  from player_standings a
order by a.wins desc, a.player_id;
