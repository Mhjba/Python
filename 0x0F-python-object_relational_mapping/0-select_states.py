#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if __name__ == '__main__':

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    # Execute query to retrieve states
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    # Display results
    for row in states:
        print(row)
