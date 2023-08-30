#!/bin/bash

echo "kubectl port-forward -n w255 service/frontend 8000:8000 --address='0.0.0.0' > output.txt"

kubectl port-forward -n w255 service/frontend 8000:8000 --address='0.0.0.0' > output.txt

echo "set up the dashboard"
echo "note this can be done in yaml"
kubectl create serviceaccount k8sadmin -n kube-system
kubectl create clusterrolebinding k8sadmin --clusterrole=cluster-admin --serviceaccount=kube-system:k8sadmin
#my_token=kubectl -n kube-system describe secret $(sudo kubectl -n kube-system get secret | (grep k8sadmin || echo "$_") | awk '{print $1}') | grep token: | awk '{print $2}'
#echo $my_token>token.txt

kubectl proxy --address='0.0.0.0' --disable-filter=true>/dev/null &
proxy_pid=$!
minikube dashboard --url >/dev/null&
echo "Open this creature:"
echo "http://localhost:8001:/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/"

