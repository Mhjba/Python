#!/usr/bin/python3
"""
changes the name of a State object to the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    Base.metadata.create_all(engine)
    state_update = session.query(State).filter_by(id='2').first()
    state_update.name = "New Mexico"
    session.commit()
