#! /usr/bin/env python

import sys
import MySQLdb
import argparse

# use argpares to parse through the arguments passed from the decPantry function in action.js
parser = argparse.ArgumentParser()
parser.add_argument("itemDec")
args = parser.parse_args()
name = args.itemDec

# open database connection
db = MySQLdb.connect("localhost","emma","sudosudo!!","pantry")

cursor = db.cursor()

# select the barcode from the name given
cursor.execute("SELECT barcode_num FROM product_list WHERE name = '%s'" % name)
result = cursor.fetchall()
barcode = result[0][0]

# update the quantity of that item
cursor.execute("SELECT quantity FROM purchases WHERE barcode_num = '%s'" % barcode)
result = cursor.fetchall()
quantity = result[0][0]
quantity -= 1

# check if new quantity is zero
if quantity == 0:
	cursor.execute("DELETE FROM purchases WHERE barcode_num = '%s'" % barcode)
# if the new quantity is not zero, just update the quantity
else:
	cursor.execute("UPDATE purchases SET quantity = '%s' WHERE barcode_num = '%s'" % (quantity, barcode))
db.commit()

db.close()


