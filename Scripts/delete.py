#! /usr/bin/env python

import MySQLdb

while True:
	barcode = raw_input("Please enter barcode: ")

	if barcode == "quit":
		break

	db = MySQLdb.connect("localhost","emma","sudosudo!!","pantry")

	cursor = db.cursor()

	cursor.execute("SELECT barcode_num FROM product_list WHERE  barcode_num = '%s'" % barcode)

	if cursor.rowcount == 0:
		print "This item does not exist"
		db.close()
	elif cursor.rowcount == 1:
		while True:
			confirm = raw_input("Are you sure you want to delete this item? (yes/no): ")
			if confirm == "yes":
				cursor.execute("DELETE FROM purchases WHERE barcode_num = '%s'" % barcode)
				if cursor.rowcount == 1:
					print "item removed from purchases successfully"
				cursor.execute("DELETE FROM product_list WHERE barcode_num = '%s'" % barcode)
				if cursor.rowcount == 1:
					print "item delete successfully"
				db.commit()
				db.close()
				break
			elif confirm == "no":
				db.close()
				break
			else:
				print "Please enter yes or no"
