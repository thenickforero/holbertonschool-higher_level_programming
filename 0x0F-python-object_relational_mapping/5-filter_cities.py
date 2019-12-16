#!/usr/bin/python3
"""Lists all cities of a certain state from the database hbtn_0e_4_usa
using certain database configuration specified via cmdline args.
"""

import sys
import MySQLdb as connector

if __name__ == "__main__":

    [db_username, db_password, db_name, state_name] = sys.argv[1:]

    connection_configuration = {
        'host': 'localhost',
        'user': db_username,
        'passwd': db_password,
        'db': db_name,
        'port': 3306
    }

    database = connector.connect(**connection_configuration)
    cursor = database.cursor()

    cursor.execute("""SELECT cities.name \
                    FROM states JOIN cities \
                    ON states.id = cities.state_id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ASC""", (state_name, ))

    result = cursor.fetchall()
    cities = [row[0] for row in result]

    print(', '.join(cities))
    cursor.close()
    database.close()
