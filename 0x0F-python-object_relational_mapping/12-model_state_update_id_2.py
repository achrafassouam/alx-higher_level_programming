#!/usr/bin/python3
"""
    Write a script that changes the name of a State object
    from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    if __name__ == "__main__":
        """
        changes the name of an object in the database
        """

        db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
            .format(
                    argv[1],
                    argv[2],
                    argv[3]
            )
        engine = create_engine(db_uri)
        Session = sessionmaker(bind=engine)

        session = Session()

        selected_state = session.query(State).filter(State.id == '2').first()
        selected_state.name = 'New Mexico'
        session.commit()
        session.close()
