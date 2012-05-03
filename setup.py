import os
import sys
import subprocess

from distutils.core import setup
from distutils.command.install import install
from distutils.command.clean import clean

class CSInstall(install):
    def run(self):
        if check_dependencies() is None:
            print 'Unable to import package `chroma`'
            sys.exit(1)

        compile_solib()
        install.run(self)

class CSClean(clean):
    def run(self):
        clean.run(self)
        clean_solib()

def compile_solib():
    '''Call `make` to compile the shared library for the ChromaPhotonList
    ROOT object.
    '''
    subprocess.call('make')

def clean_solib():
    '''Call `make clean` to clean up the C++ shared library.'''
    subprocess.call('make clean', shell=True)

def check_dependencies():
    '''Check package dependencies, since `requires` is ignored in `distutils`
    '''
    try:
        return __import__('chroma')
    except ImportError:
        return None

setup(
    name = 'chroma_server',
    version = '0.5',
    description = 'lets clients send photons to chroma for speedy propagation',
    author = 'Andy Mastbaum',
    author_email = 'mastbaum@hep.upenn.com',
    url = 'http://github.com/mastbaum/chroma-server',
    packages = ['chroma_server'],
    package_dir = {'chroma_server': 'chroma_server'},
    package_data = {'chroma_server': ['*.C', 'lib/*.so']},
    scripts = ['bin/chroma-server'],
    cmdclass = {'install': CSInstall, 'clean': CSClean}
)

