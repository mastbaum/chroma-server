import os
import distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup, find_packages, Extension

setup(
    name = 'chroma_server',
    version = '0.5',
    description = 'lets clients send photons to chroma for speedy propagation',
    author = 'Andy Mastbaum',
    author_email = 'mastbaum@hep.upenn.com',
    url = 'http://github.com/mastbaum/chroma-server',
    packages = ['chroma_server'],
    include_package_data = True,
    package_dir = {'chroma_server': 'chroma_server'},
    package_data = {'chroma_server': ['*.C']},
    scripts = ['bin/chroma_server'],
    install_requires = ['chroma']
)

