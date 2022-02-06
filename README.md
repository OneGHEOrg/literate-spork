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
- [ ] Install Python Modules ```pip install -r requirements.txt```

## Helpful commands to builds and test locally
### &nbsp; Unit Testing
- Utilize pytest plugin for visual studio code or intellij for unit testing &nbsp; or
- Execute ```pytest``` command from terminal

### &nbsp; Build
- Execute ```docker build -f Dockerfile -t mlphilli/literate-spork:latest .```

### &nbsp; Run
- Execute ```docker run -p 5001:5000 mlphilli/literate-spork:latest```
- Validate localhost:5001 is up and serving requests

### &nbsp; Push
- Execute ```docker push mlphilli/literate-spork:latest```

## Running in minikube
- [ ] Install minikube following the [minikube install guide](https://minikube.sigs.k8s.io/docs/start/)
- [ ] Start up minikube using ```minikube start```
- [ ] Deploy your app to local cluster using the following:
  - Modify [deployment.yaml](kubernetes/deployment.yaml) to include correct image:version in deployment section
  - Navigate to project root directory
  - Deploy to cluster using ```kubectl apply -f ./kubernetes/deployment.yaml```
- [ ] Enable external IP using ```minikube tunnel``` in new terminal
- [ ] Validate app via kubectl commands and/or localhost

## Cleanup locally
- [ ] Ctrl+C to stop minikube tunnel
- [ ] Execute ```minikube stop```

## Build & Deploy via Azure DevOps Pipelines
*[Azure DevOps Pipeline](https://dev.azure.com/mitchellphillips44/AzureStuff/_build?definitionId=1)*

Option 1 - Deploy from Branch
- [ ] Ensure latest code is checked in and image is set to #{BUILD_SOURCEVERSION}#
- [ ] From [ADO Pipeline](https://dev.azure.com/mitchellphillips44/AzureStuff/_build?definitionId=1)
  - Press Run in top right of page
  - Select Branch to run against
  - Press Run bottom right of page
  - Ensure "Validate App Endpoints" in Validate stage completed and returned responses

Option 2 - Run via Pull Request to Main
- [ ] Raise a PR for [literate-spork](https://github.com/mlphillips44/literate-spork) to main
- [ ] PR build will run tests and build image prior to approval
- [ ] PR will automatically deploy upon completion/merge of code
- [ ] Ensure "Validate App Endpoints" in Validate stage completed and returned responses