kubectl delete deploy/prediction-api -n mt


docker build . -t tbaums/prediction-api
docker push tbaums/prediction-api

sleep 2



kubectl apply -f prediction-api.yaml

# sleep 5
# kubectl logs -f -l app=prediction-api 

