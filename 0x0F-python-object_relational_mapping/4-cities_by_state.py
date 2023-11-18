#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]

    database = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=db_user,
            passwd=db_passwd,
            db=db_name)

    cursor = database.cursor()
    cursor.execute('SELECT cities.id, cities.name, states.name FROM cities '
                   'JOIN states ON cities.state_id = states.id '
                   'ORDER BY cities.id ASC')

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()
