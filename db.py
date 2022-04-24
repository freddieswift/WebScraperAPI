from flask import Flask
from flask_pymongo import pymongo
from app import app

#MONGO_URI
MONGO_DATABASE = "sscDatabase"
MONGO_COLL = "scrapingResult"

client = pymongo.MongoClient(MONGO_URI)
sscDatabase = client[MONGO_DATABASE]
scrapingResultColl = sscDatabase[MONGO_COLL]