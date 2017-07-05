//Database Connection
var mysql = require('mysql');

var con = mysql.createConnection({
  host: "sql9.freemysqlhosting.net",
  user: "sql9182609",
  password: "AN2ffn1RAh"
});

con.connect(function(err){
	if (err) throw err;
	console.log("Connected!");
	
	con.query("SELECT * FROM log", function(err,result){
		if(err) throw err;
		console.log("Result: "+ result)
	});
});