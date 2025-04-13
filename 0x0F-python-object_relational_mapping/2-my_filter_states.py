#!/usr/bin/env python

if __name__ == '__main__':
    import MySQLdb
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    user_input = sys.argv[4]

    db = MySQLdb.connect(user = user, passwd = passwd, database = database, port = 3306)

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE states.name = %s ORDER BY states.id""", (user_input,))

    result = cursor.fetchall()

    for state in result:
        print(state)


    cursor.close()
    db.close()
