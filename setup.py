from setuptools import setup, find_packages
import sys
import os

version = '1.1'

setup(name='MyPopcornPy',
      version=version,
      description="A script to get movies from local cinemas",
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords='',
      author='NaNkeen',
      url='',
      license='GPL-3.0+',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
