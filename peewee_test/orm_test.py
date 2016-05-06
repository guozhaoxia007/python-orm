import uuid

from peewee import *

db = MySQLDatabase('test5', host='127.0.0.1', user='root', passwd='root')


class MySQLModel(Model):
    class Meta:
        database = db


class User(MySQLModel):
    uid = CharField()
    name = CharField()
    email = CharField()

    class Meta:
        db_table = 'user'


def insert():
    uid = uuid.uuid4().hex

    user = User(uid=uid, name='gzx11', email='gzx11@gmail.com')
    user.save()


insert()
