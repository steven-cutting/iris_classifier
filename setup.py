"""
iris_classifier Copyright (C) 2017  Steven Cutting
"""

from setuptools import setup, find_packages


setup(
    name="iris_classifier",
    # Semantic versioning. MAJOR.MINOR.MAINTENANCE.(dev1|a1|b1)
    version="1.0.0",
    license='new BSD',

    description="Example for showing how to package python machine learning solutions.",

    author='Steven Cutting',
    author_email='blog@stevencutting.com',

    packages=find_packages(exclude=('bin', 'notebooks')),
    scripts=['bin/classify-iris', 'bin/mk-iris-model', 'bin/score-iris-model'],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4",
    install_requires=['scikit-learn>=0.18,<0.19',
                      'numpy>=1.13,<1.14',
                      'scipy>=0.19,<0.20',
                      'click>=6,<7',
                      'setuptools>=36,<37'],
    package_data={'': ['data/iris_model.pickle']},
    )
