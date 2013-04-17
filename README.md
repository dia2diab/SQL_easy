# SQL_easy #
---
easy way to deal with MYSQL server by using commands on terminal

# Info #
---

    - <SQL_easy> for normal user to deal with databases without writing sql syntax

    - <SQL_easy> execute SQL syntax from server and give results

    - <SQL_easy> not complete yet Soon i will add some Features such SQL Security by
    	encode passwords by some algorithms and filter the Query to prenvent SQL-injection


# Dependencies #
---
[Python][] **is required**
To install it from [Python][]'s site **OR** `sudo (apt-get|yum) install python ` for linux.

[MySQLdb][] library for Python **is required**
To install it from [MySQLdb][] for windows **OR** `sudo (apt-get|yum) python-mysqldb*` install  for linux.

# Structure #
---
[SQL_easy][]
.
├── `README.md`
├── `settings.py`
├── `hashes.py`
├── `structure.py`
├── `dealway.py`
├── `SQL_easy.py`
└── `/dump`
    *
    `{1} directories, {6} files `
    <settings.py>
        Module to set default configuration for connection to sql
        server of database.

    <hases.py>
        Module to hashe data in database for security and it will be
        option later.

    <structure.py>
        Module for DDL(Data Definition Language) commands that used to
        build, alter, and drop database objects.

    <dealway.py>
        Module for DML(Data Manipulation Language) and DRL(Data Retrieval
        Language) that used to manipilate data stored into database, it used
        to insert, update, delete and retrieve data from database.

    <SQL_easy>
        Wrapper for the whole project to merge all modules for doing task for
        user.

    <dump/>
        directory to save dumps of database on it.

    <README.md>
        it is look like manual for application for user to use it successfully.

# Screen Shot #
---
The first time you run application:
![My image](http://s14.postimg.org/bqc8mk7ch/SQL_1.png)

After set configuration settings.py and this is the main screen of app:
![My image](http://s10.postimg.org/llfx4lv6x/SQL_2.png)

Application when it is running and showing databases on server:
![My image](http://s22.postimg.org/dupc0yodt/SQL_3.png)

After using you database and this is the secondary screen of app:
![My image](http://s21.postimg.org/moogj9fqf/SQL_4.png)

[Python]: http://www.python.org/download/
[MySQLdb]: http://www.codegood.com/archives/129
