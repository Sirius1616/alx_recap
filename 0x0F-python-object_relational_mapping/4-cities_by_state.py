#!/usr/bin/env python

if __name__ == '__main__':
    import MySQLdb
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=user, password=passwd, database=database, port=3306)
    cursor = db.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC""")


    cities = cursor.fetchall()

    for city in cities:
        print(city)

