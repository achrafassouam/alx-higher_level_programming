#!/usr/bin/python3
""" write a script that takes in arguments and displays all values in states
    table of hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections
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

    sql = "SELECT * FROM states WHERE name = %s"
    params = [argv[4]]
    mycursor.execute(sql, params)

    rows = mycursor.fetchall()
    for i in rows:
        print(i)

    mycursor.close()
    db.close()
