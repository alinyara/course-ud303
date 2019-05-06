import psycopg2
from datetime import date

DBNAME = "news"

# Its necessary to create 2 different views in order to make the query results
#  Question 1 and 2
def createview1():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view question1_table as select name, title, path from (select name, title, slug from articles join authors on articles.author = authors.id) as newtable join log on log.path like concat('%', newtable.slug);")
    db.close()
# View for Question 3
def createview2():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view logerror as select date(time) as date, count(*) as total, sum(case when status != '200 OK' then 1 else 0 end) as lista from log group by date(time) order by lista;")
    db.close()

def get_three_popular():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select title, count(*) as num from question1_table group by title order by num desc limit 3;")
    data = c.fetchall()
    db.close()
    return data

print "What are the three most popular articles of all time?"
print get_three_popular();

def get_most_popular():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select name, count(*) as num from question1_table group by name order by num desc limit 3;")
    data = c.fetchall()
    db.close()
    return data

print "Who are the most popular article authors of all time?"
print get_most_popular();

def day_errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select date, cast (lista as float)/cast (total as float) as perc from logerror group by date, perc order by perc DESC limit 1;") 
    data = c.fetchall()
    db.close()
    return data

print "Which days did more than 1% of requests lead to errors?"
print day_errors();



