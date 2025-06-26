from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    HYPHEN_E_DOT='-e.'
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace("\n", "") for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements
        

setup (
    name='Fault Detection',
    version='0.0.1',
    author='sayanwita',
    author_email='dey.sayan@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
)
