#!/usr/bin/python3
"""
contains the class definition of a City
"""
from sqlalchemy import Column, ForeignKey
from model_state import Base, Integer, String


class City(Base):
    """class City"""
    __tablename__ = 'cities'
    id = Column(Integer(), primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
