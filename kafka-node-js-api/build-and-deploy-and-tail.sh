kubectl delete deploy/kafka-node-js-api

docker build . -t tbaums/kafka-node-js-api
docker push tbaums/kafka-node-js-api

sleep 2



kubectl apply -f kafka-node-js-api.yaml

sleep 15
kubectl logs -f -l app=kafka-node-js-api 

