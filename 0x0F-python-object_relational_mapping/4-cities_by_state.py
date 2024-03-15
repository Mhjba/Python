#!/usr/bin/python3
"""4. Cities by states
lists all cities from the database hbtn_0e_4_usa"""

from sys import argv
import MySQLdb

if __name__ == '__main__':

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    # Execute the query to retrieve cities
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

    rows = cur.fetchall()
    # Display the results
    for row in rows:
        print(row)
