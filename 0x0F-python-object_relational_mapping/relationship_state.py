#!/usr/bin/python3
"""Improve the files model state"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """Represents a state for a MySQL database.

    Attributes:
        __tablename__ : The name of the MySQL table to store States.
        id : The state's id.
        name : The state's name.
        cities : The State-City relationship.
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
