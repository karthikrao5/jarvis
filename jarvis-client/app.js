var app = require('express')();
var server = require('http').Server(app);
var io = require('socket.io')(server);

var sys = require("util"),
	spawn = require("child_process").spawn,
	py = spawn("python", ["../core/speech/test.py"]),
	dataString = "";

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function (socket) {
	console.log("Connected to client...");

	// as data is coming from python stream, do something here locally
	py.stdout.on('data', function(output){
		console.log("running python process");
		dataString += output.toString();
		socket.emit("serverUpdate", {data: dataString});
	});

	// do this when the python steam is over. like process the data
	// into html or something
	py.stdout.on('end', function(){
		console.log("end of python process");	
	});

	// // stringify the json input params into the python process
	// py.stdin.write(JSON.stringify(data));
	// // complete the input params
	// py.stdin.end();

	py.stderr.on("exit", (code) => {
		console.log("Process quit with code : " + code);
	})
});

// py.stdout.on("data", function(output) {
// 		var temp = String(output);
// 		io.emit("serverUpdate", {data: temp});
// 	});

server.listen(3000, function(){
  console.log('listening on port 3000');
});