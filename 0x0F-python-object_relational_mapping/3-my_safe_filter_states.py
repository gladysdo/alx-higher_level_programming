#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    search = '{}'.format(argv[4])

    """ Connect to MySQL"""
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=db_user,
        passwd=db_passwd,
        db=db_name)
    cursor = database.cursor()
    cursor.execute('SELECT id, name FROM states WHERE name = %s '
                   'ORDER BY id ASC ;', (search,))
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()
