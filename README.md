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

I tested the API via curl tool to localhost to ensure my API was working.

```curl -v http://localhost```

![image](https://user-images.githubusercontent.com/4943759/146967869-f4240397-5931-4181-bef7-8748db3a96f3.png)

## Dockerhub Container Registry and Gitlab Action Pipeline

I went to DockerHub to create an authentication token. I added the token to the secrets section and wrote a Gitlab Action YAML file to automate the build and push of this image on every push to master branch. Under Gitlab Actions, I verified my Gitlab Action Pipeline was succeeding and that the images were pushed to Docker Container Registry.

![image](https://user-images.githubusercontent.com/4943759/146968616-851ec732-320d-4c47-b05e-f0e4844e4a66.png)

![image](https://user-images.githubusercontent.com/4943759/146968888-3b093499-24b8-4faa-af40-afab0ed4b708.png)

![image](https://user-images.githubusercontent.com/4943759/146969065-3370fb73-1885-439a-9253-274df5e18575.png)

## Digital Ocean and K8s Setup

I installed the DO command line tool and created a K8s cluster via the UI.  I added the credentials to the K8s cluster to my local machine. 

I created a deployment as well as a Load Balancer Service to expose my API endpoint to the Ingress. 

Typically I would use Traefik but this is out of scope.

``` brew install doctl```

``` doctl version```

![image](https://user-images.githubusercontent.com/4943759/146969430-6e7d1435-e1a6-48ae-a144-30f5ed51d366.png)

![image](https://user-images.githubusercontent.com/4943759/146969462-01fc44fe-3fe7-4bd8-bccd-db84e201e914.png)

``` kubectl apply -f ./k8s/fastapi-deployment.yaml ```

``` kubectl apply -f ./k8s/fastapi-svc.yaml ```


I replaced my test from localhost to the External IP created by DO Load Balancer Service.

```curl -v http://165.227.250.126```

![image](https://user-images.githubusercontent.com/4943759/146969874-97db6031-1ef1-4cbe-9d6c-74d343bb1608.png)

![image](https://user-images.githubusercontent.com/4943759/146969316-2b116aea-8ecc-41c0-a74d-abff44eac4ca.png)


## ArgoCD GitOps

I installed ArgoCD into DO K8s. 

References: https://argo-cd.readthedocs.io/en/stable/getting_started/

``` kubectl create namespace argocd ```

``` kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml ```

``` kubectl apply -f ./k8s/argocd/argocd-svc.yaml -n argocd ```

I patched the argocd-server service to type Load Balancer to expose ArgoCD.

```kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'```

I navigated to the external IP and tested connectivity to argocd

![image](https://user-images.githubusercontent.com/4943759/146974462-cc0577c9-629c-4409-a175-298702c35e07.png)

