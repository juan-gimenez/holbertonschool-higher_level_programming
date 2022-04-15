#!/usr/bin/python3
"""
lists all State objects
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
    for obj in sessions.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

        for city in obj.cities:
            print("    {}: {}".format(city.id, city.name))
