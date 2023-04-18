#!/usr/bin/env python3

import version
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='robotframework-autonexuslibrary',
      version=version.VERSION,
      description='Extended Robot Framework library',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='#',
      maintainer='SQANexus',
      maintainer_email='freelanceragob@gmail.com',
      license='GPL-3.0',
      keywords='Robot Framework robot-framework selenium requests robotframework'
               'zoomba python robotframework-library api-rest api ',
      platforms='any',
      install_requires=requirements,
      classifiers="""
        Development Status :: 2 - Pre-Alpha
        Operating System :: OS Independent
        Programming Language :: Python :: 3
        Topic :: Software Development :: Testing
        Framework :: Robot Framework :: Library
        """.strip().splitlines(),
      package_dir={'': 'src'},
      packages=['AutoNexus']
      )