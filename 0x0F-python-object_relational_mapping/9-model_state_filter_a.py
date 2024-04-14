#!/usr/bin/python3
"""
    a script that lists all State objects from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    if __name__ == "__main__":
        """
        get a state from database
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

        for instance in session.query(State).filter(State.name.contains('a')):
            print('{0}: {1}'.format(instance.id, instance.name))        
