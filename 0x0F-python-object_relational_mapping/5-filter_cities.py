#!/usr/bin/python3
"""name of a state as an argument and lists all cities of that state"""

from sys import argv
import MySQLdb

if __name__ == '__main__':

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    # Execute the query safely using parameterized placeholders
    cur.execute("SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [argv[4]])
    rows = cur.fetchall()
    state = []
    # Display the results
    for row in rows:
        state.append(row[1])
    print(", ".join(state))
