#!/usr/bin/python3
"""
deletes all State objects with a name containing
the letter a from the database
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
    # Create a configured
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    Base.metadata.create_all(engine)

    state_del = session.query(State).filter(State.name.like('%a%')).all()

    # Display the result
    for delete in state_del:
        session.delete(delete)
    session.commit()
