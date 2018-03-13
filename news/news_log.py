# -*- coding: utf-8 -*-
# #!/bin/env python3.6
"""
Created on Tue Mar 13 09:53:11 2018

@author: base
"""
import psycopg2
from datetime import datetime as dt


# Function 1: What are the most popular three articles?
def popular_articles():
    """ Prints a sorted list of the three
    most popular articles of all time """

    query = """
        SELECT title, COUNT(*) as num
        FROM articlelog
        GROUP BY title
        ORDER BY num DESC
        LIMIT(3)
        """

    data = sql_query(query)
    for line in data:
        print(" * \"" + line[0] + "\" -- " + str(line[1]) + " views")


# Function 2: Who are the most popular authors?
def popular_authors():
    """ Prints a sorted list of the authors
    with the most article views """

    query = """
        SELECT name, COUNT(a.*) as num
        FROM articlelog as a
        JOIN authors as b
        ON a.author = b.id
        GROUP BY name
        ORDER BY num DESC
        """

    data = sql_query(query)
    for line in data:
        print(" * " + line[0] + " -- " + str(line[1]) + " views")


# Function 3: Which days saw more than 1% of requests being errors
def error_days():
    """ Prints a list of days where more than 1 %
    or requests to the site lead to errors """

    query = """
        SELECT a.date, (1.0*b.errors / a.all)
        FROM (SELECT DATE(time) as date, count(*) as all
              FROM log
              GROUP BY date) as a
        JOIN (SELECT DATE(time) as date, count(*) as errors
              FROM log
              WHERE status LIKE '%4%'
              OR status LIKE '%5%'
              GROUP BY date) as b
        ON a.date = b.date
        WHERE 1.0*b.errors / a.all > 0.01
        """

    data = sql_query(query)
    for line in data:
        print(" * " + line[0].strftime('%B %d, %Y') + " -- " +
              str(round(line[1] * 100, 2)) + "% errors")


def sql_query(query):
    """ takes an SQL query and returns
    query results as a list with .fetchall() """

    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    data = c.fetchall()
    c.close()
    db.close()

    return data

popular_articles()
print("---")
popular_authors()
print("---")
error_days()
