const http = require('http');
const engine = require('ejs-locals');
const express = require('express');
const bodyParser = require('body-parser');

var actions = require('/var/www/node/controllers/actions');

const PORT = 1337;
var connectionsArray = [];

var app = express();
var server = http.createServer(app);
var io = require('socket.io').listen(server);

app.use(bodyParser.urlencoded({ extended: true }));
app.engine('ejs', engine); //use ejs as the templating engine
app.set('views', __dirname + '/views');
app.use(express.static(__dirname + '/views'));

app.set('view engine', 'ejs');

server.listen(PORT, function(){
	console.log('Server started on port ' + PORT)
});

app.get('/', function (req, res){
        res.redirect('/smartfridge')
});

app.get('/smartfridge', function (req, res){
	res.render('myHTML.ejs')
});

app.post('/addDB', function (req, res){
	actions.addDB(req);
	res.redirect('/smartfridge#editdatabase');
});

app.post('/deleteDB', function (req, res){
        actions.deleteDB(req);
        res.redirect('/smartfridge#editdatabase');
});

