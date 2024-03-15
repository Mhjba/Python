#!/usr/bin/python3
"""2. Filter states by user input
takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    # Execute query to retrieve states matching the provided state name
    nmeSr = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cursor.execute(nmeSr)

    rows = cursor.fetchall()
    # Display results
    for row in rows:
        print(row)
