kubectl delete deploy/svelte-client

docker build . -t tbaums/svelte-client
docker push tbaums/svelte-client

sleep 2



kubectl apply -f svelte-client.yaml

sleep 15
kubectl logs -f -l app=svelte-client 

