import uuid

from peewee import *
from playhouse.read_slave import ReadSlaveModel


db = MySQLDatabase('test5', host='127.0.0.1', user='root', passwd='root')
read_db1 = MySQLDatabase('test4', host='127.0.0.1', user='root', passwd='root')
read_db2 = MySQLDatabase('test3', host='127.0.0.1', user='root', passwd='root')


class MySQLModel(ReadSlaveModel):
    class Meta:
        database = db
        read_slaves = (read_db1, read_db2)


class User(MySQLModel):
    id = PrimaryKeyField()
    uid = CharField(32, unique=True)
    name = CharField(20)
    email = CharField(100)

    class Meta:
        db_table = 'user'


def insert():
    uid = uuid.uuid4().hex
    User.create(uid=uid, name='gzx', email='gzx@gmail.com')


def query():
    users = User.select().order_by(User.name)
    for user in users:
        print user.name


# insert()
query()
