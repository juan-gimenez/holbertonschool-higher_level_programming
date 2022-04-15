#!/usr/bin/python3
"""
lists all City objects from the database hbtn_0e_101_usa
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
from sys import argv
from requests import Request, Session

if __name__ == '__main__':
    """
    method of sqlalchemy library
    """
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Session = sessionmaker(bind=eng)
    sessions = Session()
    for cities in sessions.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
