#! /usr/bin/env python

import sys
import MySQLdb
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("delBarcode")
args = parser.parse_args()
barcode = args.delBarcode

db = MySQLdb.connect("localhost","emma","sudosudo!!","pantry")

cursor = db.cursor()

cursor.execute("SELECT barcode_num FROM product_list WHERE barcode_num = '%s'" % barcode)

if cursor.rowcount == 1:
	cursor.execute("DELETE FROM purchases WHERE barcode_num = '%s'" % barcode)
	cursor.execute("DELETE FROM product_list WHERE barcode_num = '%s'" % barcode)
	db.commit()
db.close()
