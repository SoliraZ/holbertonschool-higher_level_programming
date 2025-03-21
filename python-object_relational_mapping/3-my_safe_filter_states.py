#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa that match
the argument and it has to be safe from mysql injections. """


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
    cusor.execute("SELECT * FROM states WHERE name = %s \
                  ORDER BY id ASC", (sys.argv[4],))
    states = cusor.fetchall()
    for state in states:
        print(state)
    cusor.close()
    db.close()
