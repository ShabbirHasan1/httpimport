from setuptools import setup

import httpimport

setup(name='httpimport',
      version=httpimport.__version__,
      description='Module for remote in-memory Python package/module loading through HTTP',
      author=httpimport.__author__,
      author_email='john.torakis@gmail.com',
      license='MIT',
      py_modules=['httpimport'],
  	  keywords = ['import', 'memory', 'http']
	  )
