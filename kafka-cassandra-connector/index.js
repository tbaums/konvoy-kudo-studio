const kafka = require('kafka-node')
const cassandra = require('cassandra-driver');
let cassandraClient

const kafkaClient = new kafka.KafkaClient({ kafkaHost: 'kafka-kafka-0.kafka-svc.default.svc.cluster.local:9093' })
const admin = new kafka.Admin(kafkaClient)
var topics = [{
    topic: 'research',
    partitions: 1,
    replicationFactor: 3
}];


var Consumer = kafka.Consumer,
    consumer = new Consumer(
        kafkaClient, [
            { topic: 'research', partition: 0 }
        ], {
            autoCommit: true
        }
    );

console.log(consumer)

try {
    cassandraClient = new cassandra.Client({ contactPoints: ['cassandra-node-0.cassandra-svc.default.svc.cluster.local:9042'], keyspace: 'research', localDataCenter: 'datacenter1' });
    console.log('Success: Connected to Cassandra')
} catch (e) {
    console.log(e)
}

consumer.on('message', function(message) {

    parsedMessage = JSON.parse(JSON.parse(message.value));

    x = parsedMessage.x;
    y = parsedMessage.y;
    uid = message.offset;
    try {
        cassandraClient.execute(`INSERT INTO coordinates (uid, x, y) VALUES (${uid} ,${x}, ${y});`);
        console.log(`Success: INSERT INTO coordinates (uid, x, y) VALUES (${uid},${x},${y})`);
    } catch (e) {
        console.log(e)
    }

});