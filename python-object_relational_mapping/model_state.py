#!/usr/bin/python3
"""This module contains the State class."""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """This class defines the states table."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
