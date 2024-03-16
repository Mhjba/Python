#!/usr/bin/python3
""" lists all State objects from the database """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

	# Connect to the engine
	engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
		argv[1], argv[2], argv[3]), pool_pre_ping=True)

	# Create a configured "Session" class
	Session = sessionmaker(bind=engine)
	# Create a Session
	session = Session()
	Base.metadata.create_all(engine)

	states = session.query(State).order_by(State.id).all()
	for state in states:
		print("{}: {}".format(state.id, state.name))
