var WebSocketServer = require('websocket').server;
var http = require('http');
var kafka = require('kafka-node')

// TODO: Rename this variable to something better
const kafka_dns = 'kafka-kafka-0.kafka-svc.' + process.env.CURRENT_POD_NAMESPACE + '.svc.cluster.local:9093'

const client = new kafka.KafkaClient({ kafkaHost: kafka_dns })
const admin = new kafka.Admin(client)
var topics = [{
    topic: 'research',
    partitions: 1,
    replicationFactor: 3
}];

try {
    admin.createTopics(topics, (err, res) => {
        // result is an array of any errors if a given topic could not be created
        console.log(res)
    })
} catch (error) {
    console.error(error)
}


var Consumer = kafka.Consumer,
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
    consumer.on('message', function(message) {
        console.log(message);
        connection.sendUTF(JSON.parse(message.value));
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
})