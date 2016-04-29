from orator import Schema

from config import db


schema = Schema(db)
# with schema.create('test') as table:
#     table.increments('id')

with schema.connection('mysql1').create('user') as table:
    table.increments('id')
    table.string('uid', 32).unique()
    table.string('name', 20)
    table.string('email', 100)

with schema.connection('mysql1').create('terminal') as table:
    table.increments('id')
    table.string('tid', 32)
    table.string('uid', 32)
    table.foreign('uid').references('uid').on('user')
