# -*- coding: utf-8 -*-
"""Model (de)serialization."""

import logging

import json

import numpy as np
from sklearn.svm import SVC

from scikit_learn_json.models import Model


class Serializer:
    """ToDo"""
    def __int__(self):
        self.svc = SVC

    def serialize(self, model: Model) -> str:
        """ToDo"""
        match type(model):
            case self.svc:
                serialized_model = self.serialize_svc(model)
            case _:
                print(f"{type(model)} not supported.")
                # ToDo: raise Error
                serialized_model = ""

        return serialized_model

    @staticmethod
    def serialize_svc(model: Model) -> str:
        """ToDo."""
        serialized_model = json.dumps({
            key: [value.tolist(), "np.ndarray", str(value.dtype)]
            if isinstance(value, np.ndarray)
            else value
            for key, value in model.__dict__.items()
        })
        return serialized_model

    @staticmethod
    def deserialize_svc(model_dict: str) -> Model:
        """ToDo."""
        model = SVC()
        model.__dict__ = {
            key: np.asarray(value[0], dtype=value[2])
            if isinstance(value, list) and value[1] == "np.ndarray"
            else value
            for key, value in json.loads(model_dict).items()
        }
        return model

    def _configure_logging(self):
        """Configure logging."""
        class_name = self.__class__.__name__
        package_name = self.__module__.split(".")[0]
        self.logger = logging.getLogger(f"{package_name}.{class_name}")
