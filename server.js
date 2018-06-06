// including http lets the server know that it will be using http to run its webpage
const http = require('http');

// EJS is a templating language that lets you embed Javascript into HTML. We need this so we can 
// access javascript scripts within the webpage itself.
const engine = require('ejs-locals');

// Express is just a module framework for Node that you can use for applications that are based 
// on server/s that will "listen" for any input/connection requests from clients.
const express = require('express');

// bodyParser is needed to parse incoming bodies (like forms) so javascript can read the client input.
const bodyParser = require('body-parser');

// Give the server a file to look to when "actions" is called.
var actions = require('/var/www/node/controllers/actions');

// The port number is telling the server what traffic to send the requests on (having it not be 
// a typical http port makes it more secure).
const PORT = 1337;

// I don't know why I need this guy, but the webpage works... so I don't ask questions.
var connectionsArray = [];

// Sets the listening function to a variable. We can now listen for specific things and 
// give them responses
var app = express();

// Sets the app (listening) variable to a server.
var server = http.createServer(app);

// Web servers run on sockets. Therefore, we need to tell the the server that it is running on a socket
var io = require('socket.io').listen(server);

// Provides a consistent API for MySQL connections
var connection = require('express-myconnection');

// We need to include mysql if we want to use it. If you were to use a different database
// you would include it in place of this include statement.
var mysql = require('mysql');


app.use(bodyParser.urlencoded({ extended: true }));

//use ejs as the templating engine
app.engine('ejs', engine);
app.set('view engine', 'ejs');

// Enables the server to see the /views and /css directories
app.set('views', __dirname + '/views');
app.use(express.static(__dirname + '/views'));
app.use(express.static(__dirname + '/css'));

// Enables the server to listen on the specified port
server.listen(PORT, function(){
	console.log('Server started on port ' + PORT)
});

// Connect to mySQL database
app.use(connection(mysql,{
	host: 'localhost',
	user: 'emma',
	password: 'sudosudo!!',
	database: 'pantry'
	}, 'pool')
);

// If the user types only the IP address with no indication of the webpage name,
// redirect to the webpage anyway.
app.get('/', function (res){
	res.redirect('/smartfridge')
});

// Client request to access the webpage with the extention "/smartfridge", call the list
// function in the actions.js file
app.get('/smartfridge', actions.list);

// Client request to add an item to the product_list table in the database. Calls the addDB function
// in actions.js file and redirects to the webpage
app.post('/addDB', function (req, res){
	actions.addDB(req);
	res.redirect('/smartfridge#editdatabase');
});

// Client request to delete an item from the product_list table in the database. Calls the deleteDB 
// function in actions.js file and redirect to the webpage
app.post('/deleteDB', function (req, res){
        actions.deleteDB(req);
        res.redirect('/smartfridge#editdatabase');
});

// Client request to add to the purchases table in the database. Calls the addPantry function in 
// actions.js file and redirects to the webpage
app.post('/addPantry', function (req, res){
        actions.addPantry(req);
        res.redirect('/smartfridge#pantry');
});

// Client request to increment an item's quantity in the purchases table in the database. Calls the
// incPantry function in the action.js file and redirect to the webpage.
app.post('/incPantry', function (req, res){
	actions.incPantry(req);
	res.redirect('/smartfridge#pantry');
});

// Client request to decrement an item's quantity in the purchases table in the database. Calls the
// decPantry function in the action.js file and redirect to the webpage.
app.post('/decPantry', function (req, res){
        actions.decPantry(req);
        res.redirect('/smartfridge#pantry');
});
