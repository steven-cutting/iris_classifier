"""
Iris classifier.
"""
__title__ = 'iris_classifier'
__author__ = 'Steven Cutting'
__author_email__ = 'steven@stevencutting.com'
__created_on__ = '06/15/2017'
__copyright__ = "iris_classifier Copyright (C) 2017  Steven Cutting"

from pkg_resources import resource_string, resource_filename
import pickle
import numpy
from sklearn import svm


load_data = numpy.loadtxt

save_data = numpy.savetxt


def mk_svc_model(x, y, kernel="rbf"):
    """
    Read docs for sklearn.svm.SVC.__init__ and sklearn.svm.SVC.fit
    """
    return svm.SVC(kernel=kernel).fit(x, y)


def score_model(model, x, y):
    return model.score(x, y)


def mk_predictor_func(model):

    def predictor_func(sepal_length, sepal_width, petal_length, petal_width):
        return model.predict([[sepal_length, sepal_width, petal_length, petal_width], ])[0]

    return predictor_func


def save_model(model, filename):
    with open(filename, "w") as f:
        pickle.dump(model, f, protocol=2)


def load_model(filename):
    with open(filename, "r") as f:
        return pickle.load(f)


# ------------------------------------------------------------------------------
# Included with the package


def load_pkg_pre_fit_model():
    """
    Load the pre-fit model that is included with the package.
    """
    return pickle.loads(resource_string(__name__, "data/iris_model.pickle"))


def load_pkg_data():
    """
    Load the data included with the package. The data that was used to fit the model.
    Returns (x_data, y_data)
    """
    try:
        return (load_data(resource_filename(__name__, "data/iris_x.csv")),
                load_data(resource_filename(__name__, "data/iris_y.csv")))
    except IOError as e:
        raise IOError("**Data Not Included In Package**: {}".format(e))
