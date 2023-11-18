#!/usr/bin/python3
""" script that takes in the name of a state"""
from sys import argv
import MySQLdb

if __name__ == '__main__':

    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=db_user,
        passwd=db_passwd,
        db=db_name)

    cursor = database.cursor()
    cursor.execute('SELECT states.name, cities.name FROM cities '
                   'JOIN states ON cities.state_id = states.id '
                   'WHERE states.name = %s '
                   'ORDER BY cities.id ASC', (state_name,))

    city_names = [row[0]for row in cursor.fetchall()]
    print(', '.join(city_names))

    cursor.close()
    database.close()
