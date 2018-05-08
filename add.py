#!/usr/bin/env python

import sys
import MySQLdb


barcode = sys.argv[1]

db = MySQLdb.connect("localhost","emma","sudosudo!!","pantry")

cursor = db.cursor()

cursor.execute("SELECT barcode_num FROM product_list WHERE barcode_num = '%s'" % barcode)

row_count = cursor.rowcount

if row_count == 0: 
	name = sys.argv[2]
	category = sys.argv[3]
	cursor.execute("INSERT INTO product_list(name, barcode_num, category) VALUES ('%s', %s, '%s')" % (name, barcode, category))
	db.commit()
db.close() 
