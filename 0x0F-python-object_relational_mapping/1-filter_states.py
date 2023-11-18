#!/usr/bin/python3
"""List all state names starting with N (case-insensitive)"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]

    """ Connect to MySQL """
    database = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=db_user,
            passwd=db_passwd,
            db=db_name)
    
    """ Create cursor object """
    cursor = database.cursor()
    
    """ Select only states starting with N """
    cursor.execute('SELECT id, name FROM states ORDER BY id ASC')

    """ Print the results """
    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)
