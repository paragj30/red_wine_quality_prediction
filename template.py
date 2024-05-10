import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "mlproject"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", #constructor needed for installing folder as a package

    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_training.py",

    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",

    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",

    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "setup.py",
    "requirements.txt",
    "research/trials.ipynb",
    "templates/index.html",
    "Dockerfile"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")