#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa
using certain database configuration specified via cmdline args.
"""

import sys
import MySQLdb as connector

if __name__ == "__main__":

    [db_username, db_password, db_name] = sys.argv[1:]

    connection_configuration = {
        'host': 'localhost',
        'user': db_username,
        'passwd': db_password,
        'db': db_name,
        'port': 3306
    }

    database = connector.connect(**connection_configuration)
    cursor = database.cursor()

    query = ('SELECT cities.id, cities.name, states.name '
             'FROM states JOIN cities '
             'ON states.id = cities.state_id '
             'ORDER BY cities.id ASC')

    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    database.close()
