#!/usr/bin/python3
""" City module """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    City class that inherits from Base class

    Attributes:
        __tablename__ (str): The name of the table.
        id (int): the unique identifier for the city (primary key).
        name (str): The name of the city.
        state_id (int): The id of the state (foreign key)

    Usage:
        Define a class that represent a city in a database
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")

    def __repr__(self):
        return f"{self.id}: {self.name}"
