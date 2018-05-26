#! /usr/bin/env python

import sys
import MySQLdb
import argparse

parser = argparse.ArgumentParseR()
parser.add_argument("barcode"
args = parser.parse_args()
barcode = args.barcode

# open database connection
db = MySQLdb.connect("localhost","emma","sudosudo!!","pantry")

cursor = db.cursor()

# check purchases list for matching barcode
cursor.execute("SELECT barcode_num FROM purchases WHERE barcode_num = '%s'" % barcode)

# if this barcode is not found in purchases
if cursor.rowcount == 0:
	# check database for a matching barcode
	cursor.execute("SELECT barcode_num FROM product_list WHERE barcode_num = '%s'" % barcode)
	# if this barcode is not in database:
#	figure out how to render a form from this file in html.
	if cursor.rowcount == 0:
#		name = raw_input("Name: ")
#		category = raw_input("Category: ")
#	break out of the python script (for now. Come back and add this functionality later)
		return
#
#
#		# add item to database
#		cursor.execute("INSERT INTO product_list(name, barcode_num, category) VALUES ('%s', '%s', '%s')" % (name, barcode, category))
#		db.commit()
	# add item to purchases list
	cursor.execute("INSERT INTO purchases(barcode_num) VALUES ('%s')" % barcode)
	db.commit()
# if the item already exists in purchases, update the quantity of that item
elif cursor.rowcount != 0:
	cursor.execute("SELECT quantity FROM purchases WHERE barcode_num = '%s'" % barcode)
	result = cursor.fetchall()
	quantity = result[0][0]
	quantity += 1
	cursor.execute("UPDATE purchases SET quantity = '%s' WHERE barcode_num = '%s'" % (quantity, barcode))
	db.commit()
db.close()

