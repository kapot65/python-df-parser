#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 12:46:59 2016

@author: chernov
"""

from setuptools import setup, find_packages
from pip.req import parse_requirements

install_reqs = parse_requirements("dfparser/requirements.txt", 
                                  session='hack')
reqs = [str(ir.req) for ir in install_reqs]

setup(
  name = 'dfparser',
  packages = find_packages(),
  version = '0.0.14',
  description = 'Parser for dataforge-envelope (http://npm.mipt.ru/dataforge/)'
  ' format.',
  author = 'Vasilii Chernov',
  author_email = 'kapot65@gmail.com',
  url = 'https://github.com/kapot65/python-df-parser',
  download_url = 'https://github.com/kapot65/python-df-parser/archive/master.zip',
  keywords = ['dataforge', 'parser'],
  install_requires=reqs,
  include_package_data=True,
  package_data = {
        '': ['*.proto'],
  },
  classifiers = [],
)
