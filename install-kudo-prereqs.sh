    
kubectl create -f https://raw.githubusercontent.com/kudobuilder/kudo/v0.4.0/docs/deployment/00-prereqs.yaml
sleep 1

kubectl create -f https://raw.githubusercontent.com/kudobuilder/kudo/v0.4.0/docs/deployment/10-crds.yaml

sleep 1

kubectl create -f https://raw.githubusercontent.com/kudobuilder/kudo/v0.4.0/docs/deployment/20-deployment.yaml

sleep 1

kubectl create -f https://raw.githubusercontent.com/kudobuilder/operators/master/repository/kafka/docs/v0.2/resources/service-monitor.yaml