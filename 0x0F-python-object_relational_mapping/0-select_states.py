#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

""" code should not be executed when imported """
if __name__ == '__main__':

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db= argv[3]
    )

    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = mycursor.fetchall()
    for i in rows:
        print(i)

    mycursor.close()
    db.close()
