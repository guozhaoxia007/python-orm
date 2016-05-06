import uuid

from schema_builder import *


def insert():
    # uid = uuid.uuid4().hex
    # User.create(uid=uid, name='gzx', email='gzx@gmail.com')

    # user = User(uid=uid, name='gzx1', email='gzx1@gmail.com')
    # user.save()

    # t1 = Terminal()
    # t1.tid = uuid.uuid4().hex
    # t1.uid = '6538629b9f26401eb650834fd6cfe664'
    # t1.save()

    # tid = uuid.uuid4().hex
    # Terminal.insert(uid='6538629b9f26401eb650834fd6cfe664', tid=tid).execute()

    # bulk insert.
    users = [
        {"uid": uuid.uuid4().hex, "name": '11', "email": '11@1.com'},
        {"uid": uuid.uuid4().hex, "name": '22', "email": '22@1.com'}]

    with db.atomic():
        # faster
        # for user in users:
        #     User.create(**user)
        # fastest
        User.insert_many(users).execute()


def query():
    users = User.select().order_by(User.name)
    for user in users:
        print user.name
    # user = User.get(User.id == 1)
    # print user, user.name


def update():
    query = User.update(name='test').where(User.id == 1)
    query.execute()


def delete():
    query = User.delete().where(User.id == 1)
    query.execute()


# #####raw sql begin#####
def query1():
    # for user in User.raw("select name from user"):
    #     print user.name

    name = 'haha'
    # Bad!
    query = User.raw('SELECT * FROM user WHERE name = "%s"' % (name,))
    print [q.name for q in query]

    # Good. `name` will be treated as a parameter to the query.
    query = User.raw('SELECT * FROM user WHERE name = %s', name)
    print [q.name for q in query]

    # Bad!
    query = User.select().where(User.name == '%s' % name)
    print [q.name for q in query]

    # Good. `name` will be treated as a parameter.
    query = User.select().where(User.name == '%s', name))
    print [q.name for q in query]


def insert1():
    uid = uuid.uuid4().hex
    name = 'abc'
    email = 'abc@gmail.com'
    db.execute_sql("INSERT INTO user(uid, name, email)"
                   "  VALUES('%s', '%s', '%s')" %
                   (uid, name, email))


def update1():
    db.execute_sql("UPDATE user SET name = 'haha' where id = 2")
# #####raw sql begin#####


# insert()
# query()
# update()
# delete()

query1()
# insert1()
# update1()
