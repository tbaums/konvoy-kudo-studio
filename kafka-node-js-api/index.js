var WebSocketServer = require('websocket').server;
var http = require('http');
var kafka = require('kafka-node'),
    Consumer = kafka.Consumer,
    client = new kafka.KafkaClient({ kafkaHost: 'kafka-kafka-0.kafka-svc.default.svc.cluster.local:9093' }),
    consumer = new Consumer(
        client, [
            { topic: 'research', partition: 0 }
        ], {
            autoCommit: true
        }
    );

console.log(consumer)


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
    consumer.on('message', function(message) {
        console.log(message);
        connection.sendUTF(message)
    });

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