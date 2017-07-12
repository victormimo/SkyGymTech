var mysql = require('mysql');

var con = mysql.createConnection({
database: "fitness",
host: "localhost",
user: "root",
password: "dataGod1996roflCopter"
});

con.connect(function(err){
if (err) throw err;
console.log("Connected!");

	con.query("SELECT * FROM log", function (err, results, fields) {
	if (err) throw err;
		console.log(results[1].exercise);
		
	});
});