#!/usr/bin/python3
""" script that lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sys import argv


if __name__ == '__main__':

    username = '{}'.format(argv[1])
    password = '{}'.format(argv[2])
    db_name = '{}'.format(argv[3])

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print('{}: {}'.format(state.id, state.name))

    session.close()
