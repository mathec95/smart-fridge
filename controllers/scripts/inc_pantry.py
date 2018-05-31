#! /usr/bin/env python

import sys
import MySQLdb
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("itemInc")
args = parser.parse_args()
name = args.itemInc

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
quantity += 1
cursor.execute("UPDATE purchases SET quantity = '%s' WHERE barcode_num = '%s'" % (quantity, barcode))
db.commit()
db.close()



