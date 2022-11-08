from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='cmdnet-backend',
    description='Backend for the CMDNET project',
    packages=find_packages(),
    install_requires=required
)