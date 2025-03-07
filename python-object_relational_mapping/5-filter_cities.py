#!/usr/bin/python3
""" Lists all cities of a state from the database hbtn_0e_4_usa. """


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cusor = db.cursor()
    cusor.execute("SELECT cities.name FROM cities JOIN states ON \
                  cities.state_id = states.id WHERE states.name = %s \
                  ORDER BY cities.id ASC", (sys.argv[4],))
    cities = cusor.fetchall()
    print(", ".join([city[0] for city in cities]))
    cusor.close()
    db.close()
