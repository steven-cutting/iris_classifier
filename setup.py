#! /usr/bin/env python
#
# iris_classifier Copyright (C) 2017  Steven Cutting
#

import sys
from setuptools import setup, find_packages
try:
    with open("README.md") as fp:
        THE_LONG_DESCRIPTION = fp.read()
except IOError:
    THE_LONG_DESCRIPTION = ''


setup(
    name="iris_classifier",
    url="https://github.com/steven-cutting/iris_classifier",
    # Semantic versioning. MAJOR.MINOR.MAINTENANCE.(dev1|a1|b1)
    version="0.0.1",
    license='new BSD',

    description="Example for showing how to package python machine learning solutions.",
    long_description=THE_LONG_DESCRIPTION,

    author='Steven Cutting',
    author_email='steven@stevencutting.com',

    classifiers=['Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'License :: OSI Approved',
                 ],
    keywords='nlp text ngram ngrams',
    packages=find_packages(exclude=('bin', 'tests', 'notebooks')),
    scripts=['bin/classify-iris', 'bin/mk-iris-model', 'bin/score-iris-model'],
    install_requires=['scikit-learn>=0.18.1',
                      ],
    extras_require={
        'test': ['pytest-runner>=2.11.1', 'pytest>=3.1.2'],
    },
    setup_requires=['pytest-runner>=2.6.2'],
    tests_require=['pytest>=2.8.7'],
    # package_data={
    #     '': ['*.json', ],
    # },
    )
