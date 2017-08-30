"""
Iris classifier.
"""
__title__ = 'iris_classifier'
__author__ = 'Steven Cutting'
__author_email__ = 'steven@stevencutting.com'
__created_on__ = '06/15/2017'
__copyright__ = "iris_classifier Copyright (C) 2017  Steven Cutting"

from iris_classifier.iris import (load_data,
                                  save_data,
                                  mk_svc_model,
                                  score_model,
                                  mk_predictor_func,
                                  save_model,
                                  load_model,
                                  load_pkg_pre_fit_model)

__all__ = [load_data, save_data,
           mk_svc_model, score_model,
           mk_predictor_func,
           save_model, load_model, load_pkg_pre_fit_model]
