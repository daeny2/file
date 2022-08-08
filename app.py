from pymongo import MongoClient
import datetime

client = MongoClient('127.0.0.1', 27017)
print(client)
db = client.Clouflake
collection = db.Clouflake

document = {"name": "이종동",
            "bio": "한국인입니다.",
            "tags": ["#몽고디비", "#파이썬", "#플라스크"],
            "date": datetime.datetime.utcnow()}


document1 = {"name": "홍길동",
            "bio": "한국인입니다.",
            "tags": ["#몽고디비", "#파이썬", "#플라스크"],
            "date": datetime.datetime.utcnow()}

document2 = {"name": "영희",
             "bio": "한국인입니다.",
             "tags": ["#MongoDB", "#Python", "#Flask"],
             "date": datetime.datetime.utcnow()}


collection.insert_one(document)

#도큐먼트 여러개 한방에 넣기
L = [document1, document2]
collection.insert_many(L)



