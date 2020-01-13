import pymongo
from pymongo import MongoClient

# Create your models here.
def mongo_connect():
    try:
        connect=MongoClient('localhost',port=27017)
        return connect.kcc_new_project
    except:
        print("error in mongo connection:",e)

db=mongo_connect()
def register_form(username,password):
    db.admin_kcc.insert({'username':username,'password':password})