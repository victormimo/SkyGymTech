var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
	
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
			//console.log(results);
			var dataset = JSON.stringify(results);
			//dataset = 5;
  			res.render('testtable', { data: dataset });
		});

	});


	
});

module.exports = router;