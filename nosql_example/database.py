from pymongo import database, MongoClient

import urllib.parse

username = urllib.parse.quote_plus('ugobest')
password = urllib.parse.quote_plus('f5IgFAiLsXOudKen')
print(username)
print(password)



uri = "mongodb://{username}:{password}@jiggy.q8wyfuv.mongodb.net/?appName=jiggy"

database = MongoClient(uri)


user_collection = database["test_db"]

collection = user_collection.users
