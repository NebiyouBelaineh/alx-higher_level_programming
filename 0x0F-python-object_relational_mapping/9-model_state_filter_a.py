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
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name.contains("%a%"))
    result = result.order_by((State.id))

    if result is None:
        print("Nothing")
    else:
        for res in result:
            print(f"{res.id}: {res.name}")
