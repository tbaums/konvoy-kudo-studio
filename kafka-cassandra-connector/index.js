const http = require('http');
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

consumer.on('message', function(message) {
    console.log(message);
});


try {
    const cassandraClient = new cassandra.Client({ contactPoints: ['cassandra-instance-node-0.cassandra-instance-svc.default.svc.cluster.local:9042'], keyspace: 'default' });
} catch (error) {
    console.log(error)
}




// cassandraClient.execute('CREATE TABLE monkeySpecies (species text PRIMARY KEY, common_name text, population varint, average_size int) WITH comment=\'User mouse streaming data\';')

// client.execute('SELECT key, email, last_name FROM user_profiles WHERE key=?', ['jbay'],
//     function(err, result) {
//         if (err) console.log('execute failed');
//         else console.log('got user profile with email ' + result.rows[0].email);
//     }
//