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
    con.query("SELECT * FROM log", function (err, results, fields) {
        if (err) throw err;
            console.log(results);

            var names = ["Jim","John","Jack","Jill"];
            /*
            var results = {
                "_id" : "100003",
                "userid" : "103",
                "projectName" : "Nodejs Project",
                "startDate" : "03/15/2015",
                "endDate" : "05/15/2015",
                "tasks" : [ 
                    {
                        "taskid" : "5",
                        "taskDescription" : "Task 5"
                    }, 
                    {
                        "taskid" : "6",
                        "taskDescription" : "Task 6"
                    }, 
                    {
                        "taskid" : "7",
                        "taskDescription" : "Task 7"
                    }
                ]
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
