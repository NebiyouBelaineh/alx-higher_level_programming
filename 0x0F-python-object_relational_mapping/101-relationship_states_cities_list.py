#!/usr/bin/python3
""" This script lists all State objects and corresponding City objects
"""

from sys import argv as av
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    engine_info = 'mysql+mysqldb://{}:{}@localhost:{}/{}'\
        .format(av[1], av[2], 3306, av[3])

    engine = create_engine(engine_info, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    total_states = session.query(State).order_by(State.id)
    for current_state in total_states:
        print(current_state)
        cities = sorted(current_state.cities, key=lambda City: City.id)
        for city in cities:
            print(f"    {city}")

    session.close()
