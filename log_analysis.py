#!/usr/bin/env python2
from datetime import datetime
import psycopg2

# Name of the database
DBNAME = "news"

# Connect to databse
db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# Query 1
# To find three most popular articles of all time
c.execute("""
SELECT articles.title, COUNT(*) AS num
FROM articles, log
WHERE log.path = '/article/' || articles.slug
GROUP BY articles.title
ORDER BY num DESC
LIMIT 3;
""")
result = c.fetchall()
print("What are the most popular three articles of all time?")

for i in range(len(result)):
    print("\n\t" + result[i][0] + " - " + str(result[i][1]) + " views")

# Query 2
# To find the most popular article authors of all time
c.execute("""
SELECT authors.name, COUNT(*) AS num
FROM authors, articles, log
WHERE log.path = '/article/' || articles.slug
AND authors.id = articles.author
GROUP BY authors.name
ORDER BY num DESC;
""")
result = c.fetchall()
print("\nWho are the most popular article authors of all time?")

for i in range(len(result)):
    print("\n\t" + result[i][0] + " - " + str(result[i][1]) + " views")

# Query 3
# To calculate which days did more than 1% of requests lead to error
# By making use of VIEW refer to readme.md
c.execute("""
SELECT date, percentage
FROM rate
WHERE rate.percentage > 1
GROUP BY date, percentage
ORDER by date;
""")
result = c.fetchall()
print("\nOn which days did more than 1% of requests lead to errors")

for i in range(len(result)):
    print("\n\t" + datetime.strptime(str(result[i][0]), "%Y-%m-%d").strftime("%B %d, %Y") +
    " - " + str("{:0.1f}".format(result[i][1])) + "% errors")



db.commit()
db.close()
