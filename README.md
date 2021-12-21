# digitalocean_k8s_challenge_2021

## Using Gitlab Actions and ArgoCD to Perform a GitOps Style Continuous Release Process & Delivery Pipeline: FastAPI Microservice to Digital Ocean Kubernetes

## 1. Creating FastAPI Base Image

First, I created a FastAPI Project. I created the Dockerfile and deployed it on localhost.

## Installing Digital Ocean Command Line Tool

``` brew install doctl```

``` doctl version```

## 1. Installing Digital Ocean Command Line Tool

``` kubectl apply -f ./k8s/fastapi-deployment.yaml ```

``` kubectl apply -f ./k8s/fastapi-svc.yaml ```

```curl -v http://165.227.250.126```

## 1. Installing Digital Ocean Command Line Tool

``` kubectl create namespace argocd ```
``` kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml ```
``` kubectl apply -f ./k8s/argocd/argocd-svc.yaml -n argocd ```