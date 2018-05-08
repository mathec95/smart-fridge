#! /usr/bin/env python

import MySQLdb

# continue to loop through code until "quit" is entered
while True:
	# query user for a barcode
	barcode = raw_input("Please enter barcode to remove from  pantry: ")

	if barcode == "quit":
		break
	# open database connection
	db = MySQLdb.connect("localhost","emma","sudosudo!!","pantry")

	cursor = db.cursor()

	# check purchases list for matching barcode
	cursor.execute("SELECT barcode_num FROM purchases WHERE barcode_num = %s" % barcode)
	# if barcode is not found in purchases list
	if cursor.rowcount == 0:
		print "This item does not exist in purchases"
	# if barcode is found in ourchases list, remove from purchases
	elif cursor.rowcount == 1:
		cursor.execute("SELECT quantity FROM purchases WHERE barcode_num = %s" % barcode)
		result = cursor.fetchall()
		quantity = result[0][0]
		# if there is only one item
		if quantity == 1:
			print "deleting item from puchases"
			cursor.execute("DELETE FROM purchases WHERE barcode_num = %s" % barcode)
			if cursor.rowcount == 1:
				print "Item successfully removed from purchases"
			db.commit()
		# if there is more than one time
		elif quantity > 1:
			print "decrementing item quantity in purchases"
			quantity -= 1
			cursor.execute("UPDATE purchases SET quantity = %s WHERE barcode_num = %s" % (quantity, barcode))
			if cursor.rowcount == 1:
				print "Item successfully updated"
			db.commit()
	db.close()
