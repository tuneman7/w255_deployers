#!/bin/bash
echo "kubectl delete -f deployment-pythonapi.yaml"
kubectl delete -f deployment-pythonapi.yaml
echo "kubectl delete -f deployment-redis.yaml"
kubectl delete -f deployment-redis.yaml
echo "kubectl delete -f service-redis.yaml"
kubectl delete -f service-redis.yaml
echo "kubectl delete -f service-prediction.yaml"
kubectl delete -f service-prediction.yaml
echo "kubectl delete -f istio-gateway-prediction.yaml"
kubectl delete -f istio-gateway-prediction.yaml
echo "kubectl delete -f namespace.yaml"
kubectl delete -f namespace.yaml
echo "kubectl delete -f prediction-grafana.yaml"
kubectl delete -f prediction-grafana.yaml

