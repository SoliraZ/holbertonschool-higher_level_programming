#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """


import MySQLdb
import sys


if __name__ == "__main__":
    """ Lists all states from the database hbtn_0e_0_usa """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
