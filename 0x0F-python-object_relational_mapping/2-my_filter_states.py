#!/usr/bin/python3
"""List all state name starting with N"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    search = argv[4]

    """ Connect to MySQL """
    database = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=db_user,
            passwd=db_passwd,
            db=db_name)
    """ Create cursor of the object """
    cursor = database.cursor()
    cursor.execute('SELECT id, name FROM states where name LIKE %s
            ORDER BY id ASC'.format(search))
    for row in cursor.fetchall():
        if row[1] == search:
            print(row)
