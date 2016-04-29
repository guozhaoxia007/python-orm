import uuid

from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from schema_builder import engine, user


conn = engine.connect()


# ###### raw sql  begin ######
def query():
    sql = "select * from user"
    res = conn.execute(sql)
    for r in res:
        print r, r.name


def insert():
    sql = "insert into user(uid, name, email) values('1111', '111', '11')"
    conn.execute(sql)


def update():
    sql = "UPDATE user SET name = '%s' where id = 1" % 'test_update'
    conn.execute(sql)


def delete():
    sql = "DELETE FROM user where id = 1"
    conn.execute(sql)
# ###### raw sql  end ######


# ###### sql expression begin ######
def query1():
    res = user.select()
    for r in conn.execute(res):
        print r


def insert1():
    uid = uuid.uuid4().hex
    name = 'test1'
    email = 'test1@gmail.com'
    # stmt = user.insert().values(uid=uid, name=name, email=email)
    stmt = user.insert(values=dict(uid=uid, name=name, email=email))
    conn.execute(stmt)


def update1():
    # stmt = user.update().values(name='test_update').where(user.c.id == 3)
    stmt = user.update(values=dict(name='test_update2')).where(user.c.id == 3)
    conn.execute(stmt)


def delete1():
    stmt = user.delete().where(user.c.id == 4)
    conn.execute(stmt)


def transcation_test():
    trans = conn.begin()
    try:
        stmt1 = user.update(values=dict(name='name123')).where(user.c.id == 9)
        stmt2 = user.insert(values=dict(uid='c50f484fb2054c5d8ba375750888f0d3', name='test', email='email'))
        conn.execute(stmt1)
        conn.execute(stmt2)

        trans.commit()
    except:
        trans.rollback()
        raise
# ###### sql expression end ######


# ###### sql expression with session begin ######
def query2():
    Session = sessionmaker(bind=engine)
    session = Session()
    # execute a string statement
    result = session.execute("select * from user where id=:id", {'id': 7})
    for r in result:
        print r, r.name

    # execute a SQL expression construct
    result = session.execute(select([user]).where(user.c.id == 9))
    for r in result:
        print r, r.name
# ###### sql expression with session end ######


insert()
# query()
# update()
# delete()

# insert1()
# query1()
# update1()
# delete1()
# transcation_test()

# query2()
