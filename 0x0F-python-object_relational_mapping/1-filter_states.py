#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""
from sys import argv
import MySQLdb

if __name__ == '__main__':

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    # Retrieve states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    # Display results
    for i in rows:
        print(i)
    # Close the cursor and database connection
    cur.close()
    db.close()
