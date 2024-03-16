#!/usr/bin/python3
"""
script that adds the State object Louisiana to the database 
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        	argv[1], argv[2], argv[3]),
		pool_pre_ping=True)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    Base.metadata.create_all(engine)

    add_state = State(name="Louisiana")
    session.add(add_state)
    session.commit()

    print(add_state.id)
