#!/usr/bin/python3

"""script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa"""

if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    # Create instance for State and City
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    # Append to new_state the new city
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()
