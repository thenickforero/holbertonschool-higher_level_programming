#!/usr/bin/python3
"""Class that represents the Cities table on the SQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """City class with a numeric ID, a name and a state id.

    Arguments:
        Base (declarative_base): Base mapped class from SQLAlchemy ORM
                                 that automatically creates a Table
                                 and a Mapper object to handle its data.
    """

    __tablename__ = 'cities'

    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
