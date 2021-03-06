#
#
# Spencer Stenger
# Log Analysis Assignment
#
# Database code for the DB log analysis
#

import datetime, psycopg2

# Database name to connect to
DBNAME = "news"

# queries for most popular three articles of all time
def popular_three_articles():
    # attempt to query for most popular three articles
    try:
        # connect to database
        connection = psycopg2.connect(database=DBNAME)
        # initiate cursor
        cursor = connection.cursor() 
        # PSQL query
        select_contents = "select articles.title, count(log.path) as num\
            from articles, log\
            where articles.slug = right(log.path, -9)\
            group by articles.title\
            order by num\
            desc limit 3"
        # execute query
        cursor.execute(select_contents)
        # return all results
        return cursor.fetchall()
        # close db connection
        connection.close()
    # throw an error if any part of the db work fails
    except:
        print("Error calculating popular three articles.")


# queries for most popular authors of all time
def popular_authors():
    try:
        connection = psycopg2.connect(database=DBNAME)
        cursor = connection.cursor()
        select_contents = "select authors.name, count(log.path) as num\
            from articles, log, authors\
            where articles.slug = right(log.path, -9)\
            and authors.id = articles.author\
            group by authors.name\
            order by num desc"
        cursor.execute(select_contents)
        return cursor.fetchall()
        connection.close()
    except:
        print("Error calculating popular authors.")


# queries for days where more than 1% of requests lead to errors
def log_errors():
    try:
        connection = psycopg2.connect(database=DBNAME)
        cursor = connection.cursor()
        select_contents = "SELECT date, ROUND((percent * 100), 1)\
            FROM\
            (SELECT DATE(time) AS date,\
            ROUND(\
            CAST(\
            SUM(\
            CASE WHEN status LIKE '40%' THEN 1 ELSE 0 END)::float/\
            COUNT(status)::float AS numeric), 3) AS percent\
            FROM log GROUP BY date) AS errorTable\
            WHERE percent > '0.01'"
        cursor.execute(select_contents)
        return cursor.fetchall()
        connection.close()
    except:
        print("Error calculating request errors.")
