from setuptools import find_packages, setup  #auto. finds all packages in our dir
from typing import List 
 
HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:  #takes the file path as string and returns a list
    #func returns list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n', "") for req in requirements]

        #do not want '-e .' stored in setup.py
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(

    name='mlproject',
    version='0.0.1',
    author='Akash',
    author_email="akashyallamati34@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)