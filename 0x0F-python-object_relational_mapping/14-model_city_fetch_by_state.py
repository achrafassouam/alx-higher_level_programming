#!/usr/bin/python3
"""
    a script that prints all City objects from the database `hbtn_0e_14_usa`
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_city import City

    if __name__ == "__main__":
        """
        accessing the database
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

        query = session.query(City, State).join(State)

        for _c, _s in query.all():
            print("{}: ({:d}) {}".format(_s.name, _c.id, _c.name))

        session.commit()
        session.close()
