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





## AWS-CICD-Deployment-with-Github-Actions

### 1. Login to AWS console.

### 2. Create IAM user for deployment

	#Policy for Identity Access Management (IAM) User with specific access:

	1. AmazonEC2ContainerRegistryFullAccess: ECR Access: Elastic Container registry to save your docker image in AWS.

	2. AmazonEC2FullAccess: EC2 access : It is virtual machine.


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to Elastic Container Registry (ECR) 

	3. Launch Your EC2 Instance

	4. Pull the image from ECR in EC2 Instance

	5. Lauch your docker image in EC2 Instance



### 3. Create ECR repo to store/save docker image
    - Save the URI of the Docker image

### 4. Create EC2 Virtual Machine (Ubuntu) 

### 5. Open EC2 and Install docker in EC2 Machine:
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
### 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


### 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app