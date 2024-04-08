import certifi
import pymongo
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId




uri = "mongodb+srv://arturmyhajlyuk:Dr0tF6nWycfkMDQc@cluster0.rplkpzm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where())

db = client.test

def find_all():
    print("All cats:")
    result = db.cats.find({})
    for el in result:
        print(el)

def find_by_name():
    print("Cats by name:")
    input_name = input("Enter name: ")
    result = db.cats.find({"name": input_name})
    for el in result:
        print(el)

def update_age_by_name():
    print("Update cat's age by name:")
    input_name = input("Enter name: ")
    input_age = input("Enter new age: ")
    db.cats.update_one({"name": input_name}, {"$set": {"age": input_age}})

def insert_new_feature():
    print("Insert new feature:")
    input_name = input("Enter name: ")
    input_feature = input("Enter new feature: ")
    db.cats.update_one({"name": input_name}, {"$push": {"features": input_feature}})

def delete_by_name():
    print("Delete cat by name:")
    input_name = input("Enter name: ")
    db.cats.delete_one({"name": input_name})

def delete_all():
    print("Delete all cats:")
    db.cats.delete_many({})

#find_all()
#find_by_name()

#update_age_by_name()
#insert_new_feature()

#delete_by_name()
#delete_all()
