kubectl delete deploy/kafka-client-api


docker build . -t tbaums/kafka-client-api
docker push tbaums/kafka-client-api

sleep 2



kubectl apply -f kafka-client-api.yaml
kubectl apply -f kafka-client-api-ingress.yaml

sleep 5
kubectl logs -f -l app=kafka-client-api 

