#!/usr/bin/env python

import sys
import MySQLdb
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("barcode")
parser.add_argument("name")
parser.add_argument("category")
args = parser.parse_args()
barcode = args.barcode
name = args.name
category = args.category

#open database connection
db = MySQLdb.connect("localhost","emma","sudosudo!!","pantry")

cursor = db.cursor()

#check the product_list for existing entry
cursor.execute("SELECT barcode_num FROM product_list WHERE barcode_num = '%s'" % barcode)

row_count = cursor.rowcount

#if this barcode is not found in product_list
if row_count == 0: 
	cursor.execute("INSERT INTO product_list(name, barcode_num, category) VALUES ('%s', %s, '%s')" % (name, barcode, category))
	db.commit()
db.close() 
