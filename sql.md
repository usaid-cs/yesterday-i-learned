# MySQL

* To install MySQL server, client, and python adapters: `sudo apt-get install mysql-common mysql-client-4.4 libmysqlclent-dev mysql-server-5.5`
* To start/stop/restart MySQL server: `(/etc/init.d/mysql OR /etc/init.d/mysqld) start/srestart`
* [Tables are stored in `/var/lib/mysql`](http://forums.mysql.com/read.php?10,239450,239465#msg-239465), and, if you are using InnoDB, the file is actually called `ibdata`.

* Create a database: [`CREATE DATABASE ebdb;`](http://dev.mysql.com/doc/refman/5.0/en/create-database.html)
  (after which you can run `python manage.py syncdb` if that happens to be your thing)
* Select a database: `USE ebdb;` (which isn't `SELECT ebdb`, for some reason)
* Delete a database: [`DROP DATABASE ebdb;`](http://dev.mysql.com/doc/refman/5.0/en/drop-database.html)
* Show list of tables: `SHOW TABLES;`

* Create an index: 


* Show tables by schema: `SELECT table_name, engine FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '(dbname)';`
* Show table columns: `SHOW COLUMNS FROM table_name;`
* Show table info: `DESCRIBE table_name;`
* Change table engine: [`ALTER TABLE table_name ENGINE=InnoDB;`](http://dev.mysql.com/doc/refman/5.5/en/converting-tables-to-innodb.html)
* Show table engines (and other info): `SHOW TABLE STATUS;`
* Show the SQL needed to create an existing table: [`SHOW CREATE TABLE table_name;`](http://stackoverflow.com/a/5615783/1558430)
* Show last `InnoDB` foreign key error: [`SHOW ENGINE INNODB STATUS;`](http://stackoverflow.com/a/179501/1558430)
* `SET unique_checks=0;` and `SET foreign_key_checks = 0;` does not help you drop a foreign key constraint.


* Create a user: `CREATE USER 'ebroot'@'localhost' [IDENTIFIED BY 'some_pass'];` (different from `CREATE USER 'ebroot';` and `CREATE USER 'ebroot'@'*';`)
* Create a user using a pre-hashed password: `CREATE USER 'ebroot'@'localhost' IDENTIFIED BY PASSWORD 'abcdef123456';`
* Give a user privileges: `GRANT ALL ON ebdb.* TO 'ebroot'@'localhost';`

* MySQL [does not](http://stackoverflow.com/a/10474104/1558430) support transactional schema alters at any time.
* Amazon [does not](https://forums.aws.amazon.com/message.jspa?messageID=153017#) allow SSH into RDS instances.
* [Why is MySQL's default collation latin1_swedish_ci?](http://stackoverflow.com/questions/6769901/why-is-mysqls-default-collation-latin1-swedish-ci)

# PostgresQL

* Logging into `psql`: `psql dbname username`
* Delete a database: (`sudo su - owner_unix_user`), then run `dropdb dbname -Uowner_unix_user -W`. Alternatively, in psql, switch to a database (`\c postgres;`), then `DROP DATABASE dbname;` to delete.
* [Postgres does not take performance hits from string lengths.](http://www.postgresql.org/docs/8.2/static/datatype-character.html) Putting it in reverse, it also means it cannot be sped up by shortening strings.
* [`varying` string type has no length limit](http://stackoverflow.com/questions/2904991/postgresql-character-varying-length-limit)
* `\c`: show the current user and database. `\c dbname` also switches to that database.
* `\d`: list tables.
* `\l`: list databases.
* Monitoring psql: `sudo tail -n 50 -f /var/log/postgresql/postgresql-9.1-main.log`
* Setting monitoring flags: [`log_min_duration_statement = 0`, and `log_statement = all`](http://stackoverflow.com/a/12670828/1558430)
* Running a SQL file: [`psql -U username -d myDataBase -a -f myInsertFile`](http://stackoverflow.com/a/12085561/1558430)

# MongoDB

MongoDB is actually NoSQL, so it shouldn't be in this file.

* Install: `sudo apt-get install mongodb`
* 

# Redis

Redis is also NoSQL. It is a KV Store, however.