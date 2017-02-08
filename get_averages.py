from pymongo import MongoClient
import csv

server = MongoClient('149.89.150.100')
#server = MongoClient('127.0.0.1')
db = server.binoculars #database
col1 = db.students #collection

peeps = col1.find()
for p in peeps:
	id = p['id']
	name = p['name']
	classes = p['classes']
	sum = 0.0
	for c in classes:
		sum += int(classes[c])
	avg = sum/(len(classes))
	print "name: %s id: %s avg: %d" %(name,id,avg)

col2 = db.teachers #another collection
tObj = open("teachers.csv")
teachers = list(csv.DictReader(tObj))

for t in teachers:
        teacher = t
        teacher['students'] = []
        sdict = col1.find()
        for s in sdict:
                if t['code'] in s['classes'].keys():
                        teacher['students'].append(s['id'])
        col2.insert_one(teacher)

tObj.close()
