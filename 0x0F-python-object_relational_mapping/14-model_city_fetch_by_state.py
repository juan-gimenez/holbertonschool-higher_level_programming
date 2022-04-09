#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
from sys import argv
from requests import Request, Session
from model_city import City

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
    obj = sessions.query(State, City).join(City).order_by(City.id).all()

    for state, city in obj:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    """
    print state city id
    and city
    """
    sessions.close()
