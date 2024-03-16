from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Converting SMILES to a list of numbers'
LONG_DESCRIPTION = 'A package that allows that Converts SMILES to a list of numbers that gives every unique atom and the atoms connected to in a number.'

# Setting up
setup(
    name="ismchem",
    version=VERSION,
    author="ismail-bc (Ismail Khalid)",
    author_email="<ismail.bootcamp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['rdkit', 'copy'],
    keywords=['python', 'chemistry', 'SMILES', 'data science],
    classifiers=[
        "Development Status :: 1 - Release",
        "Intended Audience :: Chemists/Data-scientist",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
