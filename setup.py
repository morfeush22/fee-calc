#!/usr/bin/env python

from setuptools import find_packages, setup

setup(name='fee-calc',
      version='0.1',
      install_requires=[
          'coverage(==4.4.1)',
          'Flask(==0.12.2)',
          'Jinja2(==2.9.6)',
          'libsass(==0.13.2)',
          'PasteDeploy(==1.5.2)',
          'PasteScript(==2.0.2)',
          'waitress(==1.0.2)',
          'ZODB(==5.2.4)',
      ],
      entry_points={
          'paste.app_factory': [
              'fee-calc = main:wsgi'
          ],
      },
      packages=find_packages(),
      )
