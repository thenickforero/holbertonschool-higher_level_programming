#!/usr/bin/python3
"""Prints all the cities with its state and id from a database
using SQLAlchemy with certain database configuration
specified via cmdline args.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    [db_username, db_password, db_name] = sys.argv[1:]

    connection_configuration = {
        'host': 'localhost',
        'user': db_username,
        'passwd': db_password,
        'db': db_name,
        'port': 3306
    }

    address = 'mysql://{user}:{passwd}@{host}:{port}/{db}'

    engine = create_engine(address.format(**connection_configuration))

    session_base_class = sessionmaker(engine)
    session = session_base_class()

    query = session.query(City, State).join(State).all()

    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
