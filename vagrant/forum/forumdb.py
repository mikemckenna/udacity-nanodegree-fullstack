#
# Database access functions for the web forum.
#

# import time
import psycopg2
import bleach


def GetAllPosts():
    sql = "SELECT time, content FROM posts ORDER BY time DESC"

    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    c.execute(sql)
    posts = ({'content': str(row[1]), 'time': str(row[0])}
             for row in c.fetchall())
    DB.close()
    return posts


def AddPost(content):
    sql = "INSERT INTO posts(content) VALUES(%s)"
    content_bleached = bleach.clean(content)

    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    c.execute(sql, (content_bleached,))
    DB.commit()
    DB.close()
