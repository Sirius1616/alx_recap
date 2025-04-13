#!/usr/bin/env python
"""states models
   prints all city names
   in ASCE of ID
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db_host = "localhost"
    db_user = sys.argv[1]  # "your_username"
    db_password = sys.argv[2]  # "your_password"
    db_name = sys.argv[3]  # "your_database_name"
    port = 3306

    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    cursor = db.cursor()

    cursor.execute("SELECT cities.name\
                   FROM cities LEFT JOIN states\
                   ON states.id = cities.state_id\
                   WHERE states.name = %s\
                   ORDER BY cities.id ASC", (sys.argv[4],))

    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()