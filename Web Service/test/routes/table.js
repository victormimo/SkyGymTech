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
			console.log(results[1].exercise);
			//var dataset = results;
			//dataset = 5;


  			res.render('table', { 
  				data: toString(results[1].exercise),
  				title: "The Table Page"

  			});
		});

	});


	
});

module.exports = router;