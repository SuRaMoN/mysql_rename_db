
About
=====

It's a dirty bash script to rename a database on a server (no support for moving it to another server). It is originally written by the Percona DBA Team but it has some tweaks and fixes. It only works on systems with bash installed.

Install instructions
====================

Just download the file mysql_rename_db and give it appropriate rights:
```
    wget "https://raw.githubusercontent.com/SuRaMoN/mysql_rename_db/master/mysql_rename_db"
    chmod a+x mysql_rename_db
```

You can also install it system wide by doing:
```
    git clone "https://github.com/SuRaMoN/mysql_rename_db.git"
    cd mysql_rename_db
    sudo make install
```

Usage
=====

Example:
```
    mysql_rename_db -h server -u username -pPASSWORD old_database new_database
```

All options are optional. If you eg have no password you are not required to provide one. You can pass any option that is accepted by the mysql client and mysqldump

Internal working
================

It will create the database and rename everything to the new database, at the end it will drop the old database. It will rename:

 * triggers
 * tables
 * views

RPM
===

You can create a centos/redhat RPM for it by running:
```
    git clone "https://github.com/SuRaMoN/mysql_rename_db.git"
    cd mysql_rename_db
    make rpm
```
The creation of the rpm works on both debian bases systems and redhat based systems.