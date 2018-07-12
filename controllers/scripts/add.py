#!/usr/bin/env python

import sys
import MySQLdb

#Use argparse to parse through the inputs passed by the addDB function in actions.js
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("barcode")
parser.add_argument("name")
parser.add_argument("category")
parser.add_argument("count")
args = parser.parse_args()

#set each argument equal to a variable so it can be manipulated in the script
barcode = args.barcode
name = args.name
category = args.category
count = args.count

#open database connection
db = MySQLdb.connect("localhost","emma","sudosudo!!","pantry")

#create a way to communicate with the database
cursor = db.cursor()

#check the product_list for existing entry
cursor.execute("SELECT barcode_num FROM product_list WHERE barcode_num = '%s'" % barcode)

#cursor will return any row that matches the sql statement
row_count = cursor.rowcount

#if this barcode is not found in product_list
if row_count == 0:
 	#Add the item into the product_list table
	cursor.execute("INSERT INTO product_list(name, barcode_num, category, count) VALUES ('%s', %s, '%s', '%s')" % (name, barcode, category, count))
	# save changes made to the database
	db.commit()
#close database connection
db.close()
