#!/usr/bin/python3
"""3. SQL Injection...
takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. """

from sys import argv
import MySQLdb

if __name__ == '__main__':

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    # Execute the query safely using parameterized placeholders
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])

    rows = cur.fetchall()
    # Display the results
    for row in rows:
        print(row)
