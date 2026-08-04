# it will  build ml application as package that we can install and also deploy in pypi .from pypi anybody can install it and use  it 
from setuptools import find_packages,setup
from typing import List
# find_package is used to find all the packages that are used in ml application

HYPEN_E='-e .'
def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    """
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        if(HYPEN_E in requirements):
            requirements.remove(HYPEN_E)
    return requirements

setup(
    name="ml project",
    version='0.0.1',
    author='Asmita',
    author_email='asmitashinde1176@gamil.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn'],
    install_requires=get_requirements('requirements.txt'),
)

# setup contains meta data about ml application
