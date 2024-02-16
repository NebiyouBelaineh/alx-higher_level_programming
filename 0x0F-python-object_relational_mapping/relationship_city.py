#!/usr/bin/python3
""" Python file that contains the class definition of a City."""


from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """City class:
        - inherits from Base (imported from model_state)
        - links to the MySQL table cities
        - class attribute id that represents a column of an auto-generated,
        unique integer, can’t be null and is a primary key
        - class attribute name that represents a column of a string of 128
        characters and can’t be null
        - class attribute state_id that represents a column of an integer,
        can’t be null and is a foreign key to states.id"""
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
