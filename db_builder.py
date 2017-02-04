from pymongo import MongoClient
import csv

server = MongoClient('149.89.150.100')
db = server.binoculars #database
c = db.students #collection

rcourses = open("courses.csv")
rpeeps = open("peeps.csv")
dcourses = csv.DictReader(rcourses)
dpeeps = csv.DictReader(rpeeps)
peeps = []

for x in dpeeps:
	peeps.append(x)
	
c.insert_one(peeps[0])