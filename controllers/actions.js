var mySql = require('mysql');
var PythonShell = require('python-shell');


exports.addDB = function (req) {
	var options = {
		scriptPath: '/var/www/node/controllers/scripts/',
		args: [req.body.barcode, req.body.name, req.body.category]
	}
	PythonShell.run('add.py', options, function (err, results) {
		if (err) throw err;
		console.log('results: %j', results);
	});
}

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

exports.list = function (req, res){
	req.getConnection(function(err, connection){
		var query = connection.query('SELECT product_list.name, purchases.quantity FROM purchases INNER JOIN product_list ON product_list.barcode_num=purchases.barcode_num', function(err, rows) {
			if(err)
				console.log("Error Selecting : %s ", err);
			res.render('myHTML.ejs', {page_title:"Pantry", data:rows});
		});
	});
};

exports.addPantry = function (req) {
	var options = {
		scriptPath: '/var/www/node/controllers/scripts/',
		args: [req.body.addBarcode]
	}
	PythonShell.run('add_to_pantry.py', options, function (err, results) {
		if (err) throw err;
		console.log('results: %j', results);
	});
}

