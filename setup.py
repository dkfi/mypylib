from setuptools import find_packages, setup

setup(
    name="mypylib",
    version="0.1",
    author="Kristian Du",
    description="an importable python module",
    packages=find_packages(include=['mypylib']),
    install_requires=[]
)
