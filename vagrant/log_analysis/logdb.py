# Database code for the DB log analysis

import datetime, psycopg2

DBNAME = "news"


def question_1():
    connection = psycopg2.connect(database=DBNAME)
    cursor = connection.cursor()
    select_contents = "select articles.title, count(log.path) as num from articles, log where articles.slug = right(log.path, -9) group by articles.title order by num desc limit 3"
    cursor.execute(select_contents)
    return cursor.fetchall()
    connection.close()


def question_2():
    connection = psycopg2.connect(database=DBNAME)
    cursor = connection.cursor()
    select_contents = "select authors.name, count(log.path) as num from articles, log, authors where articles.slug = right(log.path, -9) and authors.id = articles.author group by authors.name order by num desc"
    cursor.execute(select_contents)
    return cursor.fetchall()
    connection.close()


def question_3():
    connection = psycopg2.connect(database=DBNAME)
    cursor = connection.cursor()
    select_contents = "select * from log limit 1;"
    cursor.execute(select_contents)
    return cursor.fetchall()
    connection.close()
