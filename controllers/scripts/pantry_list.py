#! /usr/bin/env python

import MySQLdb
# use json so you can pass the returning information to the webpage
import json

db = MySQLdb.connect("localhost","emma","sudosudo!!","pantry")

cursor = db.cursor()

# retrieve the information for the pantry list using a join statement
cursor.execute("SELECT product_list.name, purchases.quantity, purchases.date FROM purchases INNER JOIN product_list ON purchases.barcode_num=product_list.barcode_num;")
# this line grabs the names of each column returned
row_headers=[x[0]for x in cursor.description]
data = cursor.fetchall()

json_data =[]

# loops through the returned data and applies each value to a json object
for result in data:
	json_data.append(dict(zip(row_headers,str(result))))

db.close()
