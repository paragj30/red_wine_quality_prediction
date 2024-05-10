from setuptools import find_packages,setup
from typing import List

__version__ = "0.0.0"
REPO_NAME = "red_wine_qualit_prediction"
AUTHOR_USER_NAME = "paragj30"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "paragj30@gmail.com"
HYPEN_E_DOT='-e .'


def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [file.replace("\n","") for file in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name = "End-to-end-Wine-Quality-Prediction-ML-Project-Implementation",
    version =__version__,
    author= "Parag Jadhav",
    author_email= AUTHOR_EMAIL,
    description="A small python package for ml app",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')    

)