#!/bin/bash
time minikube start --kubernetes-version=v1.25.13 --memory 16384 --cpus 4  --force
istioctl install --set profile=demo -y