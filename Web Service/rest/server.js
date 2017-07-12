// Dependancies
var express = require('express');
var bodyParser = require('body-parser');
var path = require('path');
var mysql = require('mysql');

var index = require('./routes/index');
var users = require('./routes/users');
var table = require('./routes/table');


// MySQL
var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "dataGod1996roflCopter"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});

// Express
var app = express();
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');


app.use('/', index);
app.use('/users', users);


// Routes
app.use('/api', require('./routes/api'));


//Start Server
app.listen(3000);
console.log('API is running on port 3000');
