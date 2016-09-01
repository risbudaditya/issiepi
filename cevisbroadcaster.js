var ws = require("nodejs-websocket")
var fs = require('fs');
var child_process = require('child_process');

require('events').EventEmitter.prototype._maxListeners = 20;

// ping mode flag for debugging
//var pingOn = true;
var pingOn = false;

// Johnny-Five for RPi
var raspi = require('raspi-io');
var five = require('johnny-five');
var board = new five.Board({io: new raspi()});

// Setup a server that can receive text and broadcast out.
var server = ws.createServer(function (conn) {
	console.log("New connection")
	conn.on("text", function (str) {
		console.log("Received "+str)
		conn.sendText(str.toUpperCase()+"!!!")
	})
	conn.on("close", function (code, reason) {
		console.log("Connection closed")
	})
}).listen(8001)

function broadcast(str) {
	console.log("Sending " + str);
	server.connections.forEach(function (connection) {
		connection.sendText(str)
		console.log("Sent: " + str);
	})
}

// some code to test websockets via a ping
var countOfPings = 0;
function myPing(){
	var message = countOfPings.toString();
	broadcast(message);
	console.log(message);
	countOfPings++;
}
if (pingOn) {
	setInterval(myPing,1000);
}

// Fire up the board and look for input
board.on('ready', function() {
	console.log('board is ready');

	var cevisSwitch = new five.Switch(7);
	var tickTime = Date.now();	
	cevisSwitch.on('open', function() {
		console.log('on');
    		broadcast('on');
	});

	cevisSwitch.on("close", function() {
		console.log('ping');
		broadcast('ping');
	});
});
