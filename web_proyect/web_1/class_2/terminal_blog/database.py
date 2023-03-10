import pymongo

__author__ = 'Tarrok'


class Database(object):
    URI = 'mongodb://127.0.0.1:27017'
    DATABASE = None

    @staticmethod
    def initialaize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['test']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)