from setuptools import find_packages
from setuptools import setup

setup(
    name='turtlesim_plus_scheduler',
    version='0.0.0',
    packages=find_packages(
        include=('turtlesim_plus_scheduler', 'turtlesim_plus_scheduler.*')),
)
