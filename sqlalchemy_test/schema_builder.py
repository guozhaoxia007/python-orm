from sqlalchemy import Column, Integer, String, create_engine,\
    Table, MetaData, ForeignKey


engine = create_engine('mysql://root:root@localhost:3306/test3', echo=True)

metadata = MetaData()
# metadata.bind = engine

user = Table(
    'user', metadata,
    Column('id', Integer, primary_key=True),
    Column('uid', String(32), unique=True, nullable=False),
    Column('name', String(20)),
    Column('email', String(100))
)

terminal = Table(
    'terminal', metadata,
    Column('id', Integer, primary_key=True),
    Column('tid', String(32)),
    Column('uid', String(32), ForeignKey("user.uid"), unique=True, nullable=False)
)


metadata.create_all(engine)
