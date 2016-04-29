import uuid
import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.event import listen, listens_for

from schemas_orm import User, Terminal

engine = create_engine('mysql://root:root@localhost:3306/test')
DBSession = sessionmaker(bind=engine)
session = DBSession()


def validate_email(target, value, oldvalue, initiator):
    _email_pattern = r"^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$"
    return value if re.compile(_email_pattern).match(value) else ""

listen(User.email, 'set', validate_email, retval=True)

uid = uuid.uuid4().hex
gzx = User(uid=uid, name='gzx111', email='gzx111@gmail.com')


@listens_for(User.email, 'set')
def insert():
    session.add(gzx)

    tid = uuid.uuid4().hex
    new_terminal = Terminal(tid=tid, uid=uid)
    session.add(new_terminal)

    session.commit()
    session.close()


def query():
    user = session.query(User).filter(User.id == 6).one()
    print user
    # print user.email, user.terminals
    # for t in user.terminals:
    #     print t, t.tid


def update():
    gzx = session.query(User).filter(User.id == 6).one()
    gzx.name = 'gzx_test1'
    session.commit()
    session.close()


def delete():
    gzx = session.query(User).filter(User.id == 6).one()
    session.delete(gzx)
    session.commit()
    session.close()


def transcation_test1():
    try:
        u1 = session.query(User).get(9)
        u2 = session.query(User).get(12)
        u1.name = 'u11'
        u2.name = 'u22'

        # import time
        # time.sleep(10)
        # delete from user where id = 12, commit failed!

        session.commit()
    except:
        session.rollback()
        raise


def transcation_test2():
    DBSession = sessionmaker(bind=engine, autocommit=True)
    session = DBSession()
    session.begin()
    try:
        u1 = session.query(User).get(9)
        u2 = session.query(User).get(14)
        u1.name = 'name1'
        u2.name = 'name2'

        import time
        time.sleep(10)
        # delete from user where id = 14, commit failed!

        session.commit()
    except:
        session.rollback()
        raise


def transcation_test3():
    Session = sessionmaker(bind=engine, autocommit=True)
    session = Session()
    with session.begin():
        u1 = session.query(User).get(9)
        u2 = session.query(User).get(15)

        import time
        time.sleep(10)
        # delete from user where id = 15, commit failed!
        u1.name = 'name1'
        u2.name = 'name2'


# insert()
query()
# update()
# delete()
# transcation_test1()
# transcation_test2()
# transcation_test3()
