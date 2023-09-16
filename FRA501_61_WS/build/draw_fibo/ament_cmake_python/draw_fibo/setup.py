from setuptools import find_packages
from setuptools import setup

setup(
    name='draw_fibo',
    version='0.0.0',
    packages=find_packages(
        include=('draw_fibo', 'draw_fibo.*')),
)
