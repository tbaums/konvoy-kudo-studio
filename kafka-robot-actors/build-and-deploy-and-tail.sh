kubectl delete deploy/kafka-robot-actor -n kafka-robot-actors


docker build . -t tbaums/kafka-robot-actor
docker push tbaums/kafka-robot-actor

sleep 2



kubectl apply -f kafka-robot-actor.yaml

sleep 5
kubectl logs -f -l app=kafka-robot-actor 

