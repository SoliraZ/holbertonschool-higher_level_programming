#!/usr/bin/python3
""" Module that lists all City objects from the database hbtn_0e_14_usa """


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/'
        f'{database}'
        )

    Session = sessionmaker(bind=engine)
    session = Session()
    cities = (
        session.query(City, State)
        .filter(City.state_id == State.id)
        .order_by(City.id)
        .all()
        )

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
