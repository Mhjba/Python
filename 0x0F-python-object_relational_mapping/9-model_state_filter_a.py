#!/usr/bin/python3
"""
script that lists all State objects that contain the letter a from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # Create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
