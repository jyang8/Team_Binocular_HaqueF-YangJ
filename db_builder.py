from pymongo import MongoClient
import csv

server = MongoClient('149.89.150.100')
db = server.binoculars #database
c = db.students #collection

#print c.count()

c.insert_one
