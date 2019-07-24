kubectl create -f https://raw.githubusercontent.com/kudobuilder/kudo/master/docs/deployment/00-prereqs.yaml
sleep 1

kubectl create -f https://raw.githubusercontent.com/kudobuilder/kudo/master/docs/deployment/10-crds.yaml

sleep 1

kubectl create -f https://raw.githubusercontent.com/kudobuilder/kudo/master/docs/deployment/20-deployment.yaml

sleep 1

kubectl create -f https://raw.githubusercontent.com/kudobuilder/operators/master/repository/kafka/docs/v0.1/resources/service-monitor.yaml
