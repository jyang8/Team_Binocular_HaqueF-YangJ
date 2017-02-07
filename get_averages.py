from pymongo import MongoClient
import csv

server = MongoClient('149.89.150.100')
#server = MongoClient('127.0.0.1')
db = server.binoculars #database
col = db.students #collection

peeps = col.find()
for p in peeps:
	id = p['id']
	name = p['name']
	classes = p['classes']
	sum = 0.0
	for c in classes:
		sum += int(classes[c])
	avg = sum/(len(classes))
	print "name: %s id: %s avg: %d" %(name,id,avg)
