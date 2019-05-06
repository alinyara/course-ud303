<p><b>LOG ANALYSIS PROJECT</b><BR>
Full Stack NanoDegree Program</p>

For this project, the goal is to create a reporting tool which is able to summarize the questions asked using the data that was given.

GETTING READY
- You will need to set up a virtual machine. For this project I've used Vagrant and Virtual Box;
- You will need have Pyhton 3 installed in your machine;
- Download the newsdata file from Udacity,

TO RUN
- Launch Vagrant using 'vagrant up' and after 'vagrant ssh';
- To load de data use psql -d news -f newsdata.sql
- In the psql enviroment create the views as state below:

#Question1
"def createview1():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view question1_table as select name, title, path from (select name, title, slug from articles join authors on articles.author = authors.id) as newtable join log on log.path like concat('%', newtable.slug);")
    db.close()"

#Question3
"def createview2():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view logerror as select date(time) as date, count(*) as total, sum(case when status != '200 OK' then 1 else 0 end) as lista from log group by date(time) order by lista;")
    db.close()"

- To execute the program, run python newsdb.py on the command line.


