# This is end to end wine quality prediction Machine learning project.

## Workflow

1. Update the config.yaml  
2. update the schema.yaml 
3. update the params.yaml 
4. update the entity 
5. update the configuration manager in src config
6. update the components
7. update the pipeline 
8. update the main.py
9. update the app.py file


## How to run?

### STEPS:

```bash
conda create -p venv python=3.10
```

```bash
conda activate venv
```

```bash
pip install -r "requirements.txt"
```

```bash
python app.py
```

```bash
Open the local host i.e., 0.0.0.0:8080
```

## HTML and CSS Template example:
1. https://getbootstrap.com/docs/4.0/components/forms/
2. https://colorlib.com/wp/themes/unapp/



## Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to Elastic Container Registry (ECR) 

	3. Launch Your EC2 Instance

	4. Pull the image from ECR in EC2 Instance

	5. Lauch your docker image in EC2 Instance


## AWS-CICD-Deployment-with-Github-Actions

### 0. Create the Dockerfile and CICD.yaml file

### 1. Login to AWS console.

### 2. Create IAM user for deployment

	#Policy for Identity Access Management (IAM) User with specific access:

	1. AmazonEC2ContainerRegistryFullAccess: ECR Access: Elastic Container registry to save your docker image in AWS.

	2. AmazonEC2FullAccess: EC2 access : It is virtual machine.


### 2. Create and download the Access key and Secret access key to authenticate the GitHub Action with AWS account.

    1. AWS_ACCESS_KEY_ID

    2. AWS_SECRET_ACCESS_KEY


### 3. Create ECR repository to store/save docker image

    - AWS_ECR_LOGIN_URI: Save the URI of our docker repository. This repository will be accessible to GitHub Action through this URI.

    - ECR_REPOSITORY_NAME: Save the name of the docker repository.



### 4. Create EC2 Virtual Machine (Ubuntu) 

	1. Select the "Ubuntu" OS Image as it is a lightweight virtual machine compared to the Windows VM.

	2. Select the Ubuntu Server LTS (free tier) with 64-bit architecture. 

	3. Select the Instance Type (Configurations of the Ubuntu VM Server) RAM, CPU and memory

	4. Generate the Key pair (.pem file) to securly connect to the EC2 Instance via PuttyGen/Mobaxtrem.

	5. Create a Security group by selecting the SSH, HTTP and HTTPS traffic from the internet. This group is a firewall that controls the traffic of the EC2 Instance.

        5.1 Edit the Indbound rules to  run the application. Select the "Custom TCP" and add the port number (8080).

	6. Launch the EC2 Instance.

    6. Connect to EC2 Instance using EC2 Instance Connect(launch terminal on tab) or SSH Client(3rd party client like PuttyGen/Mobaxtrem).
 
 

### 5. Open EC2 and Install docker in EC2 Machine:
	 
    ls #check if any external packages are installed or not

    clear 

	sudo apt-get update -y #To update the all package manager and dependencies in VM Instane

	sudo apt-get upgrade #To install the package manager and dependencies

    clear
	
	#required

    docker --version #To check if docker is installed or not

	curl -fsSL https://get.docker.com -o get-docker.sh #To download the docker in the EC2 virtual machine instance

    ls #To check if docker.sh file is downloaded or not. docker.sh file will have all the links and command for the docker download and installtion.

    cat get-docker.sh #To open and read the docker.sh file.

	sudo sh get-docker.sh #To run the docker.sh file. This will trigger the installation of docker.

	sudo usermod -aG docker ubuntu

	newgrp docker
	
    docker --version 

    docker ps #To check the docker images 



### 6. Configure EC2 as self-hosted runner:

    Self-hosted runner is a another VM Instance present on GitHub. So we will make a EC2 Instance as Self-hosted runner, that will make a connection with GitHub to pull the updated changes from GitHub to EC2 Instance.

    github_project>Setting>Actions>Runner>New self-hosted runner> choose os> then copy, paste and run command one by one on 'EC2 Instance Connect Terminal' to make the connection with GitHub.

    
    Enter the name of runner: self-hosted
    
    Make sure that the status of the 'self-hosted' runner is always "Idle": GitHub is connected to the EC2 Instance.



### 7. Setup github secrets:

    -So that GitHub can access the EC2 Instance.

    github_project>Setting>Actions>Secrets and variables > Actions > New repository secret > Add the below informations:
 
    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = paste the URI of the Docker repository present inside the ECR.

    ECR_REPOSITORY_NAME = simple-app



### 8. Setup .github/workflows directory inside the GitHub repository:

    -By default GitHub Actions will search the '.github/workflows' directory.

    -Create the CICD.yaml and define workflow in that file.


### 9. Open the Public URL of the Application

    -Open EC2 Instance and copy the Pubic IPv4 address and paste it in the browser URL:8080

    -Successfully deployed the application.