#!/usr/bin/python3
"""
script that prints the State object with the name passed
as argument from the database 
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

    state = session.query(State).filter(State.name == sys.argv[4]).first()
    print("Not found" if not state else state.id)
