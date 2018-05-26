#! /usr/bin/env python

import MySQLdb
import json

db = MySQLdb.connect("localhost","emma","sudosudo!!","pantry")

cursor = db.cursor()

cursor.execute("SELECT product_list.name, purchases.quantity, purchases.date FROM purchases INNER JOIN product_list ON purchases.barcode_num=product_list.barcode_num;")
row_headers=[x[0]for x in cursor.description]
data = cursor.fetchall()

json_data =[]

for result in data:
	json_data.append(dict(zip(row_headers,str(result))))

print json_data
db.close()
