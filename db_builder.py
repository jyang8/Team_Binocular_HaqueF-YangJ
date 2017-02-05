from pymongo import MongoClient
import csv

server = MongoClient('149.89.150.100')
#server = MongoClient('127.0.0.1')
db = server.binoculars #database
col = db.students #collection

pObj = open("peeps.csv")
peeps = list(csv.DictReader(pObj))
cObj = open("courses.csv")
courses = list(csv.DictReader(cObj))

for p in peeps:
	student = p
	for c in courses:
		if p['id'] == c['id']:
			student[c['code']] = c['mark']
	col.insert_one(student)
