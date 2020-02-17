const kafka = require('kafka-node')
const cassandra = require('cassandra-driver');

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

const cassandraClient = new cassandra.Client({ contactPoints: ['cassandra-instance-node-0.cassandra-instance-svc.default.svc.cluster.local:9042'], keyspace: 'data', localDataCenter: 'datacenter1' });

consumer.on('message', function(message) {

    parsedMessage = JSON.parse(JSON.parse(message.value));

    x = parsedMessage.x;
    y = parsedMessage.y;
    uid = message.offset;
    console.log(`INSERT INTO coordinates (uid, x, y) VALUES (${uid},${x},${y})`)
    cassandraClient.execute(`INSERT INTO coordinates (uid, x, y) VALUES (${uid} ,${x}, ${y})`).catch();
});