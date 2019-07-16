kubectl delete deploy/kafka-dummy-actor


docker build . -t tbaums/kafka-dummy-actor
docker push tbaums/kafka-dummy-actor

sleep 2



kubectl apply -f kafka-dummy-actor.yaml

sleep 5
kubectl logs -f -l app=kafka-dummy-actor 

