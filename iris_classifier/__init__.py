"""
Iris classifier.
"""
__title__ = 'iris_classifier'
__author__ = 'Steven Cutting'
__author_email__ = 'steven@stevencutting.com'
__created_on__ = '06/15/2017'
__copyright__ = "iris_classifier Copyright (C) 2017  Steven Cutting"

import pickle
import numpy
from sklearn import linear_model, svm

__all__ = []


load_data = numpy.loadtxt

save_data = numpy.savetxt

# iris = datasets.load_iris()
# X_iris = iris.data
# y_iris = iris.target

# n_samples = len(X_iris)

# X_train = X_iris[:int(.9 * n_samples)]
# y_train = y_iris[:int(.9 * n_samples)]
# X_test = X_iris[int(.9 * n_samples):]
# y_test = y_iris[int(.9 * n_samples):]


def mk_logistic_model(x, y):
    """
    Read docs for sklearn.linear_model.LogisticRegression.__init__ and
    sklearn.linear_model.LogisticRegression.fit
    """
    return linear_model.LogisticRegression().fit(x, y)


def mk_svc_model(x, y, kernel="rbf"):
    """
    Read docs for sklearn.svm.SVC.__init__ and sklearn.svm.SVC.fit
    """
    return svm.SVC(kernel=kernel).fit(x, y)


def score_model(model, x, y):
    return model.score(x, y)


def mk_predictor_func(model):
    return model.predict


def save_model(model, filename):
    with open(filename, "w") as f:
        pickle.dump(model, f, protocol=2)


def load_model(filename):
    with open(filename, "r") as f:
        return pickle.load(f)
