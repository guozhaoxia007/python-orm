# from orator import DatabaseManager
from orator_cache import DatabaseManager, Cache


config = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'test',
        'user': 'root',
        'password': 'root',
        'prefix': '',
        'log_queries': True
    },
    'mysql1': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'test4',
        'user': 'root',
        'password': 'root',
        'prefix': '',
        'log_queries': True
    }
}

stores = {
    'stores': {
        'redis': {
            'driver': 'redis',
            'host': '192.168.3.206',
            'port': 6379,
            'db': 0
        }
    }
}

cache = Cache(stores)

db = DatabaseManager(config, cache)
