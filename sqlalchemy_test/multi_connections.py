import random
import uuid

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

from orm_schema import Terminal, User


engines = {
    'master': create_engine("mysql://root:root@localhost:3306/test"),
    'terminal': create_engine("mysql://root:root@localhost:3306/test1"),
    'slave1': create_engine("mysql://root:root@localhost:3306/test2"),
    'slave2': create_engine("mysql://root:root@localhost:3306/test3"),
}


class RoutingSession(Session):
    def get_bind(self, mapper=None, clause=None):
        if mapper and issubclass(mapper.class_, Terminal):
            return engines['terminal']
        elif self._flushing:
            return engines['master']
        else:
            return engines[
                random.choice(['slave1', 'slave2'])
            ]

Session = sessionmaker(class_=RoutingSession)
session = Session()


def insert():
    # engine bind db:test
    uid = uuid.uuid4().hex
    u1 = User(uid=uid, name='u1', email='u1@gmail.com')
    session.add(u1)
    session.commit()
    session.close()


def query_terminal():
    # engine bind db:test1
    terminal = session.query(Terminal).get(1)
    print terminal


def query_user():
    # engine bind db:test2 or test3
    user = session.query(User).get(6)
    print user


# insert()
query_terminal()
query_user()
