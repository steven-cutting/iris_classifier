"""
iris_classifier Copyright (C) 2017  Steven Cutting
"""

from setuptools import setup, find_packages


setup(
    name="iris_classifier",
    # Semantic versioning. MAJOR.MINOR.MAINTENANCE.(dev1|a1|b1)
    version="0.0.1",
    license='new BSD',

    description="Example for showing how to package python machine learning solutions.",

    author='Steven Cutting',
    author_email='steven@stevencutting.com',

    packages=find_packages(exclude=('bin', 'notebooks')),
    scripts=['bin/classify-iris', 'bin/mk-iris-model', 'bin/score-iris-model'],
    install_requires=['scikit-learn>=0.18.1',
                      'numpy>=1.13.0',
                      'scipy>=0.19.0',
                      ],
    package_data={'': ['iris_y.csv',
                       'iris_x.csv',
                       'iris_model.pickle']},
    )
