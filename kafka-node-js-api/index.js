// var app = require('express')();
// var http = require('http').createServer(app);
// var io = require('socket.io')(http);

// const port = 3002


// app.get('/kafka-node-js-api', function(req, res) {
//     res.send('<h1>Hello world</h1>');
// });


// io.on('connection', function(socket) {
//     console.log('user connected');

//     socket.on('disconnect', function() {
//         console.log('user disconnected');
//     });

//     socket.on('add-message', (message) => {
//         io.emit('message', { type: 'new-message', text: message });
//     });
// });

// http.listen(port, function() {
//     console.log('listening on port ' + port);
// });

var WebSocketServer = require('websocket').server;
var http = require('http');

var server = http.createServer(function(request, response) {
    // process HTTP request. Since we're writing just WebSockets
    // server we don't have to implement anything.
});
server.listen(3002, function() {});

// create the server
wsServer = new WebSocketServer({
    httpServer: server
});



// WebSocket server
wsServer.on('request', function(request) {
    var connection = request.accept(null, request.origin)
    connection.sendUTF("pongo")

    // This is the most important callback for us, we'll handle
    // all messages from users here.
    connection.on('message', function(message) {
        if (message.type === 'utf8') {
            // process WebSocket message
        }
    });

    connection.on('close', function(connection) {
        // close user connection
    });
});