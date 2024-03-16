#!/usr/bin/python3
"""
Improve the files model city
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class State(Base):
    """Represents a city for a MySQL database.

    Attributes:
        id : The city's id.
        name : The city's name.
        state_id : The city's state id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
