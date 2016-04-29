from orator import DatabaseManager


config = {
    'mysql': {
        'read': [{
            'host': 'localhost',
            'database': 'test1',
            'user': 'root',
            'password': 'root'
        }],
        'write': [{
            'host': 'localhost',
            'database': 'test',
            'user': 'root',
            'password': 'root',
        }],
        'driver': 'mysql',
        'prefix': ''
    }
}

db = DatabaseManager(config)
results = db.select('select * from user')
print results
