var app = require('express')();
var http = require('http').createServer(app);
var io = require('socket.io')(http);

const port = 3002


app.get('/', function(req, res) {
    res.send('<h1>Hello world</h1>');
});


io.on('connection', (socket) => {
    console.log('user connected');

    socket.on('disconnect', function() {
        console.log('user disconnected');
    });

    socket.on('add-message', (message) => {
        io.emit('message', { type: 'new-message', text: message });
    });
});

http.listen(port, function() {
    console.log('listening on port ' + port);
});