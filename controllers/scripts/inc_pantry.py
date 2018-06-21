#! /usr/bin/env python

import sys
import MySQLdb
import argparse

# use argparse to parse through arguments passed by incPantry function in actions.js
parser = argparse.ArgumentParser()
parser.add_argument("itemInc")
args = parser.parse_args()
name = args.itemInc

# open database connection
db = MySQLdb.connect("localhost","emma","sudosudo!!","pantry")

cursor = db.cursor()

# select the barcode and count per package from the name given
cursor.execute("SELECT barcode_num, count FROM product_list WHERE name = '%s'" % name)
result = cursor.fetchall()
barcode = result[0][0]
count = result[0][1]

# update the quantity of that item with the count given
cursor.execute("SELECT quantity FROM purchases WHERE barcode_num = '%s'" % barcode)
result = cursor.fetchall()
	# cursor.fetchall will return a double array of rows of the table.
quantity = result[0][0]
quantity += count
cursor.execute("UPDATE purchases SET quantity = '%s' WHERE barcode_num = '%s'" % (quantity, barcode))
db.commit()
db.close()



