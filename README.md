quotes_database
===============
prepareDB.py
-------------
It should be runned first of all.

example:
>$python2.7 prepareDB.py "path/to/new/database" "type of database"

tested on *type of database*==sqlite


addToDB.py
-------------
It should be runned in the same directory where *added.log* file exist (if you start it first time you should have a "empty file"). Python script will add to lod-file all absolutes pathes of sql files wich wass successfuly added to database (it don't know to what database, so if you add file to one database you can't add it to another database).

example:
>$python2.7 addToDB.py "path/to/dir/with/sql/files" "path/to/database" "application name"
tested on *application name*==sqlite3

Also you can run it with *--help* flag to see the help mgs