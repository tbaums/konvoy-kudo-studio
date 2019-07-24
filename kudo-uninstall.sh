kubectl delete -f https://raw.githubusercontent.com/kudobuilder/kudo/master/docs/deployment/00-prereqs.yaml

kubectl delete -f https://raw.githubusercontent.com/kudobuilder/kudo/master/docs/deployment/10-crds.yaml

kubectl delete -f https://raw.githubusercontent.com/kudobuilder/kudo/master/docs/deployment/20-deployment.yaml

kubectl delete pvc --all