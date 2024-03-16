#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the db
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
        # Create a Session
    session = Session()

    state = session.query(State).filter(State.name == argv[4]).first()

    # Display the result
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
