from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True)
    uid = Column(String(32))
    name = Column(String(20))
    email = Column(String(100))
    terminals = relationship('Terminal')

    @property
    def columnitems(self):
        return dict([(c, getattr(self, c)) for c in self.columns])

    def tojson(self):
        return self.columnitems


class Terminal(Base):
    __tablename__ = 'terminal'

    id = Column(Integer(), primary_key=True)
    tid = Column(String(32))
    uid = Column(String(32), ForeignKey('user.uid'))
