#!/usr/bin/python3
"""Add a new state called Louisiana to a database using SQLAlchemy
with certain database configuration specified via cmdline args
and prints its id.
"""

import sys
from model_state import Base, State
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

    new_row = State(name='Louisiana')

    session.add(new_row)
    session.commit()

    print(new_row.id)
