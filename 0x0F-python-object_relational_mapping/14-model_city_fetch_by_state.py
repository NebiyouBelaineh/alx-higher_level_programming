#!/usr/bin/python3

"""script that lists all State objects from the database hbtn_0e_6_usa"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine, select
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    join_condition = State.id == City.state_id
    selected = select(State.name.label('state_name'), City.id.label('city_id'),
                      City.name.label('city_name')).select_from(State)
    joined = selected.join(City, join_condition).order_by(City.id)
    results = session.execute(joined).fetchall()

    for res in results:
        print(f"{res.state_name}: ({res.city_id}) {res.city_name}")
