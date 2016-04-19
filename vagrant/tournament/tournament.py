#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach
import itertools


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    sql = "DELETE FROM matches;"
    conn = connect()
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    sql = "DELETE FROM players;"
    conn = connect()
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    sql = "SELECT COUNT(*) FROM players"

    conn = connect()
    c = conn.cursor()
    c.execute(sql)
    result = c.fetchone()
    conn.close()

    # print result
    # print result[0]
    # print type(result)
    return result[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    sql = "INSERT INTO players(name) VALUES (%s)"
    name_bleached = bleach.clean(name)

    conn = connect()
    c = conn.cursor()
    c.execute(sql, (name_bleached,))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    sql = "SELECT * FROM player_standings ORDER BY wins desc, player_id"

    conn = connect()
    c = conn.cursor()
    c.execute(sql)
    result = c.fetchall()
    conn.close()

    # print result
    # print type(result)
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    sql = "INSERT INTO matches(winner_id, loser_id) VALUES (%s, %s)"

    conn = connect()
    c = conn.cursor()
    c.execute(sql, (winner, loser,))
    conn.commit()
    conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    standings_scrubbed = [(a, b) for a, b, c, d in standings] # create new tuple list with only (id, name)
    pairings = [player1 + player2 for (player1, player2) in itertools.izip(standings_scrubbed[::2], standings_scrubbed[1::2])]

    # print standings
    # print standings_scrubbed
    # print pairings
    return pairings
