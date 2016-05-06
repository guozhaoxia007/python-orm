from peewee import *

db = MySQLDatabase('test5', host='127.0.0.1', user='root', passwd='root')


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


class Terminal(MySQLModel):
    id = PrimaryKeyField()
    tid = CharField(32, unique=True)
    # db_column is needed, otherwise column will be ended with _id
    uid = ForeignKeyField(User, to_field='uid', db_column='uid')

    class Meta:
        db_table = 'terminal'


# User.create_table()
# Terminal.create_table()
# db.create_tables([User, Terminal], safe=True)
