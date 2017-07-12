var express = require('express');
var router = express.Router();
var mysql = require('mysql');

/* GET home page. */
router.get('/', function(req, res, next) {
	
    
    /* DATABSE CONNECT */
    var con = mysql.createConnection({
    database: "fitness",
    host: "localhost",
    user: "root",
    password: "dataGod1996roflCopter"
    });

    con.connect(function(err){
        if (err) throw err;
        console.log("Connected!");
    });

    /* SELECT DATA */
    con.query("SELECT *, DATE_FORMAT(date_added, \"%m-%d-%Y\") AS date_mod FROM log;log", function (err, results, fields) {
        if (err) throw err;
            console.log(results);

            var names = ["Jim","John","Jack","Jill"];
            /*
            var results = {
                "entry_id" : "100003",
                "exercise" : "103",
                "reps" : "Nodejs Project",
                "sets" : "03/15/2015",
                "weight" : "05/15/2015",
                "avg_vel" : "05/15/2015",
                "entry_RFID" : "05/15/2015",
                "date_added" : "05/15/2015",
            };
            */
            var int = 4;
            res.render('index', { 
                title: 'Express',
                guests: names,
                number: int,
                data: results

            });








            //var dataset = results;
            //dataset = 5;
    });

	
    
    con.end(function(err){
    });
});

module.exports = router;
