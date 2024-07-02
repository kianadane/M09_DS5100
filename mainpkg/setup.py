import pandas as pd
from setuptools import setup, find_packages

setup(
    name='Test',
    version='0.0.1',
    url='https://github.com/kianadane/DS5100_M09.git',
    author='K. Dane',
    author_email='urn8he@virginia.edu',
    description='to print hello world!',
    packages= find_packages(),
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)