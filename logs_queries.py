#!/usr/bin/env python3
import psycopg2

# Database queries

# Query no. 1: 3 most popular articles of all time
query_1_title = ("3 most popular articles of all time:")
query_1 = """select articles.title, count(*) as num
            from log, articles
            where log.status='200 OK'
            and articles.slug = substr(log.path, 10)
            group by articles.title
            order by num desc
            limit 3;"""

# Query no. 2: the authors of most popular articles
query_2_title = ("The most popular article authors of all time:")
query_2 = """select authors.name, count(*) as num
            from articles, authors, log
            where log.status='200 OK'
            and authors.id = articles.author
            and articles.slug = substr(log.path, 10)
            group by authors.name
            order by num desc;
            """

# Query no. 3: the days when more than 1% of requests lead to errors
query_3_title = ("The days on which more than 1 percent of requests lead to errors:")
query_3 = """
    select * from (
        select a.day,
        round(cast((100*b.hits) as numeric) / cast(a.hits as numeric), 2)
        as errperc from
            (select date(time) as day, count(*) as hits from log group by day) as a
            inner join
            (select date(time) as day, count(*) as hits from log where status
            like '%404%' group by day) as b
        on a.day = b.day)
    as t where errperc > 1.0;"""

# establish the database connection
def connect(database_name="news"):
    """Connect to the PostgreSQL database. Returns a database connection object"""
    try:
        db = psycopg2.connect("dbname=news")
        cursor = db.cursor()
        return db, cursor
    except:
        print("Failed to connect to the database")

# get results of all the queries and manually close database connection, just for safety reasons
def get_query_results(query):
    """Return query results for a particular query """
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()

# print query results
def print_query_results(query_results):
    print (query_results[1])
    for index, results in enumerate(query_results[0]):
        print(str(index + 1) + '. ' + str(results[0]) + ': ' + str(results[1]) + ' views')

# print erroneous results
def print_error_results(query_results):
    print (query_results[1])
    for results in query_results[0]:
        print('On ' + str(results[0]) + ' '+ str(results[1]) + '% of requests lead to errors')

# create the views
if __name__ == '__main__':
    # store query results in the views
    popular_articles_results = get_query_results(query_1), query_1_title
    popular_authors_results = get_query_results(query_2), query_2_title
    load_error_days = get_query_results(query_3), query_3_title

    # print query results
    print_query_results(popular_articles_results)
    print_query_results(popular_authors_results)
    print_error_results(load_error_days)
