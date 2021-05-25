from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='gtki_api',
    version='0.1',
    packages=find_packages(),
    author='PunchyArchy',
    author_email='ksmdrmvscthny@gmail.com',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    install_requires=[
        'gravity_core_api_cm_beta'
    ],
)
