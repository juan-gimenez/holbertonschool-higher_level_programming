#!/usr/bin/python3
"""
creates the State “California” with the City “San Francisco”
"""
from relationship_state import Base, State
from relationship_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

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
    obj = State(name="California")
    obj.cities = [City(name="San Francisco")]
    """
    create state w city
    """
    session.add(obj)
    session.commit()
    session.close()
