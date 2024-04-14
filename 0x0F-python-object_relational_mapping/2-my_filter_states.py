#!/usr/bin/python3
""" Write a script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

""" code should not be executed when imported """
if __name__ == '__main__':

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
    )

    mycursor = db.cursor()

    sql = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])

    mycursor.execute(sql)

    rows = mycursor.fetchall()
    for i in rows:
        print(i)

    mycursor.close()
    db.close()
