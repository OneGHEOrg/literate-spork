# Demo App for Liatrio Working Exercise

This application will act as a live exercise for gauging technical compentency as well as collaboration skills of Mitchell Phillips.

## Prerequisites
- [ ] Clone repository from [literate-spork](https://github.com/mlphillips44/literate-spork)
- [ ] Install Python version 3.10 or greater
  - MacOs: ```brew install python@3.10```
  - Windows: ```choco install python```
  - Linux (Ubuntu) ```sudo apt-get update && sudo apt-get install python```
- [ ] Install Pip
  - MacOs/Linux:  ```python -m pip install --upgrade pip```
  - Windows: ```py -m pip install --upgrade pip```
- [ ] Install Python Modules
  - Change working directory to /utensils
  - ```pip install -r requirements.txt```

## Helpful commands to builds and test locally
### &nbsp; Unit Testing
- Utilize pytest plugin for visual studio code or intellij for unit testing &nbsp; or
- Navigate to project root directory, execute ```pytest``` command from terminal

### &nbsp; Build
- Navigate to utensils directory
- Execute ```docker build -f ../docker/Dockerfile -t mlphilli/spork-fest:latest .```

### &nbsp; Run
- Execute ```docker run mlphilli/literate-spork:latest```
- Validate endpoint:port are up and accessible

### &nbsp; Push
- Execute ```docker push mlphilli/literate-spork:<tag-name>```

## Running in minikube
- [ ] Install minikube following the [minikube install guide](https://minikube.sigs.k8s.io/docs/start/)
- [ ] Start up minikube using ```minikube start```
- [ ] Deploy your app to local cluster using the following:
  - Modify [deployment.yaml](kubernetes/deployment.yaml) to include correct image:version in deployment section
  - Navigate to project root directory
  - Deploy to cluster using ```kubectl apply -f ./kubernetes/deployment.yaml```
- [ ] Enable external IP using ```minikube tunnel``` in new terminal
- [ ] Validate app via kubectl commands and/or localhost

## Build & Deploy via Azure DevOps Pipelines
TODO: Work on this section