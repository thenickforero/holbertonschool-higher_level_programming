#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa
only if its matches name with a certain state
using certain database configuration specified via cmdline args.

P.S this script is safe from MySQL injections.
"""

import sys
import MySQLdb as connector

if __name__ == "__main__":

    [db_username, db_password, db_name, searched_state_name] = sys.argv[1:]

    connection_configuration = {
        'host': '127.0.0.1',
        'user': db_username,
        'passwd': db_password,
        'db': db_name,
        'port': 3306
    }

    database = connector.connect(**connection_configuration)
    cursor = database.cursor()

    query = ('SELECT * FROM states '
             'WHERE name LIKE BINARY %s '
             'ORDER BY states.id ASC')

    cursor.execute(query, (searched_state_name,))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    database.close()
