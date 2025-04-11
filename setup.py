from setuptools     import setup, find_packages
from setuptools.command.build_py import build_py
from setuptools.command.install import install
from typing import List
import os

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
    


setup(
    name="random",
    version="0.0.1",
    author="Swajay Nandanwade",
    author_email="swajaynandanwade04@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),

    


)