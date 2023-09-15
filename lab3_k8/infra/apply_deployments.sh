#!/bin/bash

echo "kubectl create -f namespace.yaml"
kubectl create -f namespace.yaml
echo "kubectl apply -f deployment-redis.yaml"
kubectl apply -f deployment-redis.yaml
echo "kubectl apply -f service-redis.yaml"
kubectl apply -f service-redis.yaml
echo "kubectl apply -f deployment-pythonapi.yaml"
kubectl apply -f deployment-pythonapi.yaml
echo "kubectl apply -f service-prediction.yaml"
kubectl apply -f service-prediction.yaml
echo "kubectl apply -f istio-gateway-prediction.yaml"
kubectl apply -f istio-gateway-prediction.yaml
echo "kubectl apply -f prediction-grafana.yaml"
kubectl apply -f prediction-grafana.yaml
echo "kubectl apply -f telemetry.yaml"
kubectl apply -f telemetry.yaml