import uuid

from config import db


# ###### raw sql begin ######
def query():
    # results = db.select('select * from user')
    results = db.select("select * from user where id = %s" % 6)
    print results


def insert():
    uid = uuid.uuid4().hex
    # db.insert("insert into user(uid, name, email) values ('%s', '%s', '%s')" %
    #           (uid, 'John', 'john@gmail.com'))
    db.insert("insert into user(uid, name, email) values (%s, %s, %s)",
              [uid, 'John', 'john@gmail.com'])


def update():
    db.update("update user set name = %s where id = %s", ['test', 6])


def delete():
    db.delete("delete from user where id = %s", [25])
# ###### raw sql end ######


# ###### query builder begin ######
def query1():
    # retrieving all row from a table
    users = db.table('user').get()
    # users = db.table('user').select('name', 'email').get()
    # users = db.table('user').distinct().get()
    # users = db.table('user').select('name as user_name').get()
    # users = db.table('user').where('id', '>', 10).get()
    for user in users:
        print user

    # chunking results from a table
    # users = db.table('user').chunk(3)
    # print users
    # for user in users:
    #     print user

    # retrieving a single row from a table
    # user = db.table('user').where('name', 'John').first()
    # print user

    # retrieving a single column from a row
    # user = db.table('user').where('name', 'John').pluck('name')
    # print user

    # retrieving a list of column values
    # users = db.table('user').lists('name')
    # users = db.table('user').lists('email', 'name')
    # print users

    # with cache
    # users = db.table('user').remember(10).get()
    # print users


def insert1():
    uid = uuid.uuid4().hex
    # db.table('user').insert(uid=uid, name='a', email='a@bar.com')

    # db.table('user').insert({
    #     'uid': uid,
    #     'name': 'b',
    #     'email': 'b@bar.com'
    # })

    db.table('user').insert([
        {'uid': 111, 'name': '111', 'email': '111@bar.com'},
        {'uid': 222, 'name': '222', 'email': '222@bar.com'}
    ])


def update1():
    # db.table('user').where('id', 6).update(name='123')

    db.table('user').where('id', 6).update({'name': '234'})


def delete1():
    db.table('user').where('id', '=', 29).delete()
    # db.table('user').delete()
    # db.table('user').truncate()


def transcation():
    with db.transaction():
        db.table('user').where('id', 26).update({'name': 'hehe'})
        db.table('user').insert([
            {'uid': 111, 'name': '111', 'email': '111@bar.com'},
            {'uid': 222, 'name': '222', 'email': '222@bar.com'}
        ])


def transcation2():
    db.begin_transaction()
    try:
        db.table('user').where('id', 26).update({'name': 'hehe'})
        db.table('user').insert([
            {'uid': 111, 'name': '111', 'email': '111@bar.com'},
            {'uid': 222, 'name': '222', 'email': '222@bar.com'}
        ])
        db.commit()
    except:
        db.rollback()
        raise
# ###### query builder end ######


# query()
# insert()
# update()
# delete()
# transcation()
# transcation2()

query1()
# insert1()
# update1()
# delete1()
