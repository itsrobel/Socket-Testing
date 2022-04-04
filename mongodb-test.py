#!/usr/bin/env python3
from pymongo import MongoClient
import datetime

client = MongoClient()
db = client.test_database

post = {
    "author": "Mike",
    "text":"The first text",
    "date": datetime.datetime.utcnow()
}

posts = db.post
post_id = posts.insert_one(post).inserted_id
print(post_id)
