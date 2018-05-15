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
