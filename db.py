import pymongo

from db_config import *


class Db:
    def __init__(self):
        self.client = pymongo.MongoClient(SERVER, PORT)
        self.user_db = self.client[DATABASE]


db = Db()
config = db.user_db.config
movies = db.user_db.movies


def setup_config(config_type):
    return config.insert_one(CONFIGS[config_type])


def get_config(config_type):
    row = config.find_one(CONFIGS[config_type])
    if not row:
        setup_config(config_type)
    return config.find_one(CONFIGS[config_type])
