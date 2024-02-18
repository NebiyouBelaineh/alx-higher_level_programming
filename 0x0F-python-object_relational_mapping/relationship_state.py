#!/usr/bin/python3
""" State module """

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base class

    Attributes:
        __tablename__ (str): The name of the table.
        id (int): the unique identifier for the state (primary key).
        name (str): The name of the state.
        cities (relationship): the cities in a state

    Usage:
        Define a class that represent a state in a database
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, unique=True,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete")

    def __repr__(self):
        """ This method return a string representaion of an instance
        """
        return "{}: {}".format(self.id, self.name)
