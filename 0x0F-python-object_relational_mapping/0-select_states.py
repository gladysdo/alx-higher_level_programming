#!/usr/bin/python3
""" List all state in the database """

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]

    """Connect to MySQL server"""
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=db_user,
        passwd=db_passwd,
        db=db_name
    )

    """Create a cursor object"""
    cursor = database.cursor()

    """Execute the SQL query"""
    cursor.execute('SELECT * FROM states ORDER BY id ASC')

    """Fetch and display"""
    for row in cursor.fetchall():
        print(row)
