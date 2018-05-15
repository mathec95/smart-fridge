#! /usr/bin/env python

import MySQLdb

# continue to loop through code until "quit" is entered
while True:
	# query user for a barcode
	barcode = raw_input("Please enter barcode to add to pantry:")

	if barcode == "quit":
		break
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
		if cursor.rowcount == 0:
			name = raw_input("Name: ")
			category = raw_input("Category: ")
			# add item to database
			cursor.execute("INSERT INTO product_list(name, barcode_num, category) VALUES ('%s', '%s', '%s')" % (name, barcode, category))
			if cursor.rowcount == 1:
				print "item added to database successfully"
			db.commit()
		# add item to purchases list
		cursor.execute("INSERT INTO purchases(barcode_num) VALUES ('%s')" % barcode)
		if cursor.rowcount == 1:
			print "item added to purchases successfully"
		db.commit()
	# if the item already exists in purchases, update the quantity of that item
	elif cursor.rowcount != 0:
		cursor.execute("SELECT quantity FROM purchases WHERE barcode_num = '%s'" % barcode)
		result = cursor.fetchall()
		quantity = result[0][0]
		quantity += 1
		cursor.execute("UPDATE purchases SET quantity = '%s' WHERE barcode_num = '%s'" % (quantity, barcode))
		if cursor.rowcount == 1:
			print "item quantity updated successfully"
		db.commit()
	db.close()

