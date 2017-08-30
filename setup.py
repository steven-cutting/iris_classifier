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
    author_email='steven@stevencutting.com',

    packages=find_packages(exclude=('bin', 'notebooks')),
    scripts=['bin/classify-iris', 'bin/mk-iris-model', 'bin/score-iris-model'],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4",
    install_requires=['scikit-learn>=0.18.1',
                      'numpy>=1.13.0',
                      'scipy>=0.19.0',
                      'click>=6.7.0',
                      ],
    package_data={'': ['data/iris_model.pickle']},
    )
