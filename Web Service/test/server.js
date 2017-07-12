var express = require('express'),

app = express(),
port = process.env.PORT || 3000;

app.get('/',function(req,res){
	res.send('Working!')
})

app.listen(port);

console.log('Test app RESTful API server started on: ' + port);