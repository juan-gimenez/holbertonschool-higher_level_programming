#!/usr/bin/python3
"""
list all states with letter "a"
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
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    sessions = Session()
    obj = sessions.query(State).order_by(State.id)
    for state in obj:
        if "a" in obj:
            print("{}: {}".format(state.id, state.name))
    sessions.close()
