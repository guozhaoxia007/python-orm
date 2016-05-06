from peewee import *
from playhouse.pool import PooledMySQLDatabase


db = PooledMySQLDatabase(
    'test5',
    max_connections=32,
    stale_timeout=300,  # 5 minutes.
    host='127.0.0.1',
    user='root',
    password='root')


class MySQLModel(Model):
    class Meta:
        database = db


class User(MySQLModel):
    id = PrimaryKeyField()
    uid = CharField(32, unique=True)
    name = CharField(20)
    email = CharField(100)

    class Meta:
        db_table = 'user'


def query():
    users = User.select().order_by(User.name)
    for user in users:
        print user.name


query()
