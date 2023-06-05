
var express = require('express');
var app = express();
var bodyParser = require('body-parser');  
var cors = require('cors')

// Create application/x-www-form-urlencoded parser  
app.use(express.static('public')); 
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: false
}));
app.use(cors());
const multer = require('multer')

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'images/')
  },
  filename: (req, file, cb) => {
    cb(null, "pic.jpg")
  },
})

const upload = multer({ storage: storage })


app.post('/name',upload.single('file'), callName);


function callName(req, res) {

	var spawn = require("child_process").spawn;
	console.log(" app listening started")  

	var process = spawn('python',["./main.py"] );
  console.log(" preprocessing started") 
	process.stdout.on('data', function(data) {
		res.send(JSON.stringify(data.toString()));
	} )
}
var server = app.listen(3200, function () {  
    var host = server.address().address  
    var port = server.address().port  
    console.log(" app listening at http://%s:%s", host, port)  
  })  
