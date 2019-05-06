# Log Analysis

This is the 3rd project in the Full Stack NanoDegree of Udacity. For this project, the goal is to create a reporting tool which is able to summarize the questions asked using the data that was given.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.    

### Prerequisites

To run this program, will you **need**:
- You will need to set up a virtual machine. For this project, download [Vagrant]([Vagrant](https://www.vagrantup.com/"Vagrant") and [Virtual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1); 
- You will to download [Python](https://www.python.org/ftp/python/3.7.3/python-3.7.3-macosx10.9.pkg) and install this in your machine;
- Download the newsdata file. Please [click here to download it.](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)  

### To run

- Launch Vagrant using 'vagrant up' and after 'vagrant ssh';
- To load de data use psql -d news -f newsdata.sql

#### Create the views

This view will be used to answer question 1 and 2.
```
    createview1():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view question1_table as select name, 
    title, path from (select name, title, slug from articles 
    join authors on articles.author = authors.id) as newtable 
    join log on log.path like concat('%', newtable.slug);")
    db.close()
```

This view will be used to answer question 3.
```
    createview2():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view logerror as select date(time) as date, 
    count(*) as total, sum(case when status != '200 OK' then 1 else 0 end) 
    as lista from log group by date(time) order by lista;")
    db.close()
```
#### Execute

To execute the program, run **python newsdb.py** on the command line.
