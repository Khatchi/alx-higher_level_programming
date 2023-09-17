#!/usr/bin/python3
"""
This module lists all the states in the
database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    connect = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    """
    Connect to MySQL database.
    """

    cursor = connect.cursor()
    """
    Creates a cursor object to interact with the database.
    """

    cursor.execute("SELECT * FROM states")
    """Executes MySQL querry."""

    rows = cursor.fetchall()
    """Fetches all the selected rows."""

    for row in rows:
        print(row)
