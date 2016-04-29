import uuid

from orator import Model
from orator.orm import has_many, belongs_to

from config import db


Model.set_connection_resolver(db)


class User(Model):
    __table__ = 'user'
    __timestamps__ = False

    @has_many('uid', 'uid')
    def terminal(self):
        return Terminal


class Terminal(Model):
    __table__ = 'terminal'
    __timestamps__ = False

    @belongs_to('uid', 'uid')
    def user(self):
        return User


def query():
    # case 1
    # users = User.all()
    # converting a model to a dictionary
    # users = User.all().serialize()
    # print users
    # for user in users:
    #     print user, user.name
    # case 2
    # user = User.find(6)
    # converting a model to json
    user = User.find(6).to_json()
    print user
    # case 3
    # count = User.where('id', '=', 6).count()
    # print count

    # user = User.where('id', '>', 10).first_or_fail()
    # print user, user.name

    # users = User.where('id', '>', 1).take(3).get()
    # for user in users:
    #     print(user.name)

    # users = User.where_raw("id > %s and name = 'John'", [3]).get()
    # print users
    # for user in users:
    #     print user.id, user.name

    # specifying the query connection
    # user = User.on('mysql1').find(6)
    # user = User.on_write_connection().find(1)
    # print user

    # terminals = User.find(6).terminal
    # print terminals
    # for terminal in terminals:
    #     print terminal.tid

    # user = Terminal.find(1).user
    # print user, user.name


def insert():
    user = User()
    user.name = 'John1'
    user.uid = uuid.uuid4().hex
    user.email = 'john1@gmail.com'
    user.save()

    # Create a new user in the database
    # user = User.create(name='John')

    # Retrieve the user by attributes, or create it if it does not exist
    # user = User.first_or_create(name='John')

    # Retrieve the user by attributes, or instantiate it if it does not exist
    # user = User.first_or_new(name='John')


def update():
    # user = User.find(6)
    # user.name = 'Foo'
    # user.save()

    affected_rows = User.where('id', '>', 28).update(name='test')
    print affected_rows


def delete():
    # user = User.find(28)
    # user.delete()

    affected_rows = User.where('id', '>', 27).delete()
    print affected_rows


query()
# insert()
# update()
# delete()
