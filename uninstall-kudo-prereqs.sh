kubectl delete -f https://raw.githubusercontent.com/kudobuilder/kudo/v0.4.0/docs/deployment/00-prereqs.yaml
sleep 1

kubectl delete -f https://raw.githubusercontent.com/kudobuilder/kudo/v0.4.0/docs/deployment/10-crds.yaml

sleep 1

kubectl delete -f https://raw.githubusercontent.com/kudobuilder/kudo/v0.4.0/docs/deployment/20-deployment.yaml

kubectl delete pvc --all