#!/usr/bin/env python

if __name__ == '__main__':
    import MySQLdb
    import sys


    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host = 'localhost', user = user, passwd = passwd, db = database, port = 3306)


    cur = db.cursor()

    cur.execute('SELECT * FROM states')

    result = cur.fetchall()
    for state in result:
        print(state)

