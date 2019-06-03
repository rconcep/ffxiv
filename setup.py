from setuptools import setup, find_packages
from distutils.core import Extension

DISTNAME = 'FFXIV Sim'
VERSION = '0.1'
EXTENSIONS = []
PYTHON_REQUIRES='>=36'
DESCRIPTION = ''
LONG_DESCRIPTION = open('README.md').read()
AUTHOR = ''
MAINTAINER_EMAIL = 'rconcep@sandia.gov'
LICENSE = ''
URL = ''

setuptools_kwargs = {
    'scripts': [],
    'include_package_data': True,
    'install_requires' : ['numpy', 'pandas>=0.24.2',
                          'matplotlib',]
}

setup(name=DISTNAME,
      version=VERSION,
      packages=find_packages(),
      ext_modules=EXTENSIONS,
      python_requires=PYTHON_REQUIRES,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      maintainer_email=MAINTAINER_EMAIL,
      license=LICENSE,
      url=URL,
      **setuptools_kwargs)