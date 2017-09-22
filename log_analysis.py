#!/usr/bin/env python2
import psycopg2

DBNAME = "news"


def db_connect():
    """ Creates and returns a connection to the database defined by DBNAME,
        as well as a cursor for the database.

        Returns:
            db, c - a tuple. The first element is a connection to the database.
                    The second element is a cursor for the database.
    """

    # Your code here
    # Connect to databse
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    return c, db


def execute_query(query):
    """execute_query takes an SQL query as a parameter.
        Executes the query and returns the results as a list of tuples.
       args:
           query - an SQL query statement to be executed.

       returns:
           A list of tuples containing the results of the query.
    """

    # Your code here
    c, db = db_connect()
    c.execute(query)
    result = c.fetchall()
    return result
    db.commit()
    db.close()


def print_top_articles():
    """Prints out the top 3 articles of all time."""

    query = """
    SELECT title, views
    FROM articles
    INNER JOIN
        (SELECT path, count(path) AS views
        FROM log
        GROUP BY log.path) AS log
        ON log.path = '/article/' || articles.slug
        ORDER BY views DESC
        LIMIT 3;
    """

    results = execute_query(query)

    # add code to print results
    print("What are the most popular three articles of all time?")

    for title, views in results:
        print('\n\t{} - {} views'.format(title, views))


def print_top_authors():
    """Prints a list of authors ranked by article views."""
    query = """
    SELECT authors.name, COUNT(*) AS num
    FROM authors, articles, log
    WHERE log.path = '/article/' || articles.slug
    AND authors.id = articles.author
    GROUP BY authors.name
    ORDER BY num DESC;
    """

    results = execute_query(query)

    # add code to print results
    print("\nWho are the most popular article authors of all time?")

    for title, views in results:
        print('\n\t{} - {} views'.format(title, views))


def print_errors_over_one():
    """Prints out the days where more than 1% of logged
    access requests were errors."""
    query = """
    SELECT date, percentage
    FROM rate
    WHERE rate.percentage > 1
    GROUP BY date, percentage
    ORDER by date;
    """
    results = execute_query(query)

    # add code to print results
    print("\nOn which days did more than 1% of requests lead to errors")

    for date, error_percent in results:
        print(
            '\n\t{0:%B %d, %Y} - {1:.1f}% errors'.format(date, error_percent))

if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_errors_over_one()
