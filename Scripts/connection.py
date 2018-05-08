#!/usr/bin/env python

import MySQLdb

db = MySQLdb.connect("localhost","emma","sudosudo!!","pantry")

cursor = db.cursor()

cursor.execute("SELECT * FROM product_list")

data = cursor.fetchall()

print data

db.close()
