var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var http = require('http');
var fs  = require('fs');
var sys = require('sys');

var index = require('./routes/index');
var users = require('./routes/users');

var app = express();
app.use(express.logger());

/*
app.set("view options", {layout: false});
app.use(express.static(__dirname + '/views'));
*/


// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'hjs');


// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', index);
app.use('/users', users);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});


/*
//CONNECT DATABASE
var mysql = require('mysql');

var con = mysql.createConnection({
	database: "fitness",
	host: "localhost",
	user: "root",
	password: "dataGod1996roflCopter"
});

//CALL RESULTS
con.connect(function(err){
	if (err) throw err;
	console.log("Connected!");

	con.query("SELECT * FROM log", function (err, result, fields) {
		if (err) throw err;
		// console.log(result);
  		//console.log(result[1].exercise)
		//var outputresult = result;
	});

});

function onRequest(req, res){
	res.writeHead(200,{'Content-Type': 'text/plain'});
	res.write("Hello");
	res.end();
};
*/

//HOME
/*
app.get("/", function(req, res) {
	//res.render('/views/testtable.hjs')
});

app.get("/about", function(req, res) {
  res.end("Welcome to the about page!");
});

app.get("*", function(req, res) {
  res.end("404!");
});
*/

app.listen(8000);

//module.exports = app;