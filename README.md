# Using Gitlab Actions and ArgoCD to Perform a GitOps Style Continuous Release Process 
## FastAPI Microservice to Digital Ocean Kubernetes

### FastAPI and Docker

I created a FastAPI API Project. I created the Dockerfile and deployed it on localhost.

![image](https://user-images.githubusercontent.com/4943759/146966873-9c1a0664-b9b1-4839-aa4f-5126be0cb401.png)
![image](https://user-images.githubusercontent.com/4943759/146967012-5a3d04f8-a41b-4de2-8d6a-90cd36c26dd8.png)

References: https://fastapi.tiangolo.com/deployment/docker/

Commands: 
```docker build -t fastapi .```

```docker run -d --name fastapi_helloworld -p 80:80 fastapi```

![image](https://user-images.githubusercontent.com/4943759/146967761-58e55d10-09ee-40f3-8f99-855712bb49c0.png)
![image](https://user-images.githubusercontent.com/4943759/146967829-bc93208d-1268-4726-93b7-3a35fa8645f7.png)

```curl -v http://165.227.250.126```

![image](https://user-images.githubusercontent.com/4943759/146967869-f4240397-5931-4181-bef7-8748db3a96f3.png)

## Dockerhub Container Registry and Gitlab Action Pipeline

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
