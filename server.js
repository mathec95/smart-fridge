const http = require('http');
const engine = require('ejs-locals');
const express = require('express');
const bodyParser = require('body-parser');
//const spawn = require('child_process').spawn;

var actions = require('/var/www/node/controllers/actions');

const PORT = 1337;
var connectionsArray = [];

var app = express();
var server = http.createServer(app);
var io = require('socket.io').listen(server);
var connection = require('express-myconnection');
var mysql = require('mysql');

app.use(bodyParser.urlencoded({ extended: true }));
app.engine('ejs', engine); //use ejs as the templating engine
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/css'));
app.use(express.static(__dirname + '/views'));

server.listen(PORT, function(){
	console.log('Server started on port ' + PORT)
});

app.use(connection(mysql,{
	host: 'localhost',
	user: 'emma',
	password: 'sudosudo!!',
	database: 'pantry'
	}, 'pool')
);

app.get('/', function (req, res){
	res.redirect('/smartfridge')
});

app.get('/smartfridge', actions.list);

app.post('/addDB', function (req, res){
	actions.addDB(req);
	res.redirect('/smartfridge#editdatabase');
});

app.post('/deleteDB', function (req, res){
        actions.deleteDB(req);
        res.redirect('/smartfridge#editdatabase');
});

app.post('/addPantry', function (req, res){
        actions.addPantry(req);
        res.redirect('/smartfridge#pantry');
});

app.post('/incPantry', function (req, res){
	actions.incPantry(req);
	res.redirect('/smartfridge#pantry');
});

app.post('/decPantry', function (req, res){
        actions.decPantry(req);
        res.redirect('/smartfridge#pantry');
});


