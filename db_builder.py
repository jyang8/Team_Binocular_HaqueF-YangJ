from pymongo import MongoClient
import csv

server = MongoClient('149.89.150.100')
db = server.binoculars #database
c = db.students #collection

#print c.count()

courses = open("courses.csv")
peeps = open("peeps.csv")
dcourses = csv.dictReader(courses)
dpeeps = csv.dictReader(peeps)

for x in dcourses:
        c.insert_one(x);
