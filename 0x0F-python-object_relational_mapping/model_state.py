#!/usr/bin/python3
"""Class that represents the State table on the SQLAlchemy ORM
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State class with a numeric ID and name.

    Arguments:
        Base (declarative_base): Base mapped class from SQLAlchemy ORM
                                 that automatically creates a Table
                                 and a Mapper object to handle its data.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
