from setuptools import setup, find_packages
from typing import List

hypen_e_dot = '-e .'

def get_requirements(file_path:str) -> list[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","").strip() for req in requirements]
        requirements = [req for req in requirements if req != hypen_e_dot]
            
    return requirements

setup(
    name='student-score-prediction',
    version='0.0.1',
    author='Sai Varsha',
    author_email='saivarshadevoju@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)