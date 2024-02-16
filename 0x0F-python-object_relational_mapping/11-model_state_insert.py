#!/usr/bin/python3

"""script that lists all State objects from the database hbtn_0e_6_usa"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    state = State(name="Louisiana")
    state.name = "Louisiana"

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(state)
    session.commit()

    result = session.query(State.id).filter(State.name == "Louisiana").first()

    if result is None:
        print("Not found")
    else:
        print(f"{result.id}")
