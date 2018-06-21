// We will be using mysql to connect to the database
var mySql = require('mysql');

// We will use python-shell to run python scripts
var PythonShell = require('python-shell');

// If the server calls the addDB function, run the python script with the barcode, name, and 
// category user inputs
exports.addDB = function (req) {
	var options = {
		scriptPath: '/var/www/node/controllers/scripts/',
		args: [req.body.barcode, req.body.name, req.body.category, req.body.quantity]
	}
	PythonShell.run('add.py', options, function (err, results) {
		if (err) throw err;
		console.log('results: %j', results);
	});
}

// If the server calls the deleteDB function, run the python script with the barcode user input
exports.deleteDB = function (req) {
        var options = {
                scriptPath: '/var/www/node/controllers/scripts/',
                args: [req.body.delBarcode]
        }
        PythonShell.run('delete.py', options, function (err, results) {
                if (err) throw err;
                console.log('results: %j', results);
        });
}

// If the server calls the list function, request the pantry list using a SQL join statement
// and render the home webpage with the returned data
exports.list = function (req, res){
	req.getConnection(function(err, connection){
		var query = connection.query('SELECT product_list.name, purchases.quantity FROM purchases INNER JOIN product_list ON product_list.barcode_num=purchases.barcode_num', function(err, rows) {
			if(err)
				console.log("Error Selecting : %s ", err);
			res.render('myHTML.ejs', {page_title:"Pantry", data:rows});
		});
	});
};

// if the server calls the addPantry function, run the the python script with the barcde user input
exports.addPantry = function (req) {
	var options = {
		scriptPath: '/var/www/node/controllers/scripts/',
		args: [req.body.addPantryBarcode]
	}
	PythonShell.run('add_to_pantry.py', options, function (err, results) {
		if (err) throw err;
		console.log('results: %j', results);
	});
}

// If the server calls te incPantry function, run the python scripts with the item name as input
exports.incPantry = function (req) {
	var options = {
		scriptPath: '/var/www/node/controllers/scripts/',
		args: [req.body.itemInc]
	}
	PythonShell.run('inc_pantry.py', options, function (err, results) {
		if (err) throw err;
		console.log('results: %j', results);
	});
}

// If the server calls the decPantry function, run the python scripts with the item name as input
exports.decPantry = function (req) {
        var options = {
                scriptPath: '/var/www/node/controllers/scripts/',
                args: [req.body.itemDec]
        }
        PythonShell.run('dec_pantry.py', options, function (err, results) {
                if (err) throw err;
                console.log('results: %j', results);
        });
}
