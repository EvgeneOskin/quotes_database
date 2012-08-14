quotes_database
===============
prepareDB.py
------------
It should be runned first of all.

example:
>$python2.7 prepareDB.py "path/to/new/database" "type of database"

tested on *type of database*==sqlite


addToDB.py
----------
example:
>$python2.7 addToDB.py "path/to/dir/with/sql/files" "path/to/database" "application name"

It will create a file *path/to/database*.log. Python script will add to log-file all absolutes pathes of sql files wich wass successfuly added to database 

tested on *application name*==sqlite3

Also you can run it with *--help* flag to see the help mgs