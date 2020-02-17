kubectl delete deploy/kafka-cassandra-connector

docker build . -t tbaums/kafka-cassandra-connector
docker push tbaums/kafka-cassandra-connector

sleep 2



kubectl apply -f kafka-cassandra-connector.yaml

sleep 15
kubectl logs -f -l app=kafka-cassandra-connector 

