"""This allows you to run `pip install .` in this directory and any local packages you've created can be installed"""

from setuptools import setup, find_packages

setup(
    name='mudtek',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your package's dependencies here
    ]
)