#! /usr/bin/env python

import sys
import MySQLdb
import argparse

# use argparse to parse through the arguments passed by the delDB function in action.js
parser = argparse.ArgumentParser()
parser.add_argument("delBarcode")
args = parser.parse_args()
barcode = args.delBarcode

#create connection to the database
db = MySQLdb.connect("localhost","emma","sudosudo!!","pantry")

cursor = db.cursor()

#check product_list table for existing entry
cursor.execute("SELECT barcode_num FROM product_list WHERE barcode_num = '%s'" % barcode)

#cursor will return any row that matches the sql statement
#if there is a matching entry in the database
if cursor.rowcount == 1:
	# delete from purchases and product_list. The first execution will not always go through
	# because not every product_list item will be in purchases. This does not create an error.
	cursor.execute("DELETE FROM purchases WHERE barcode_num = '%s'" % barcode)
	cursor.execute("DELETE FROM product_list WHERE barcode_num = '%s'" % barcode)
	db.commit()
db.close()
