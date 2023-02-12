# -*- coding: utf-8 -*-
"""Model (de)serialization."""

import logging

import json

from pathlib import Path
import os
from typing import Dict, Union
import numpy as np
from sklearn.svm import SVC

from scikit_learn_json.models import Model
from scikit_learn_json.exceptions import ModelNotSupported


class Serializer:
    """ToDo"""
    svc = SVC

    def __int__(self):
        """Initialization."""
        self._configure_logging()

    def serialize(self, model: Model, out_json_file: str) -> bool:
        """ToDo"""
        match type(model):
            case self.svc:
                serialized_model = self._serialize_svc(model)
            case _:
                print(f"{type(model)} not supported.")
                # ToDo: raise Error
                serialized_model = ""

        with open(out_json_file, "w") as model_json:
            json.dump(serialized_model, model_json)

        return os.path.isfile(out_json_file)

    def deserialize(self, json_file: Union[str, Path]) -> Model:
        """ToDo"""
        with open(json_file) as file:
            model_dict = json.load(file)

        model_type = model_dict["model_type"]
        model_parameter = model_dict["model_parameter"]
        match model_type:
            case "SVC":
                model = self._deserialize_svc(model_parameter)
            case _:
                raise ModelNotSupported(f"'{model_type}' is not supported.")

        return model

    @staticmethod
    def _serialize_svc(model: Model) -> Dict:
        """ToDo."""
        model_dict = {"model_type": "SVC"}
        serialized_model = {
            key: [value.tolist(), "np.ndarray", str(value.dtype)]
            if isinstance(value, np.ndarray)
            else value
            for key, value in model.__dict__.items()
        }
        model_dict["model_parameter"] = serialized_model
        return model_dict

    @staticmethod
    def _deserialize_svc(model_dict: dict) -> Model:
        """ToDo."""
        model = SVC()
        model.__dict__ = {
            key: np.asarray(value[0], dtype=value[2])
            if isinstance(value, list) and value[1] == "np.ndarray"
            else value
            for key, value in zip(model_dict.keys(), model_dict.values())
        }
        return model

    def _configure_logging(self):
        """Configure logging."""
        class_name = self.__class__.__name__
        package_name = self.__module__.split(".")[0]
        self.logger = logging.getLogger(f"{package_name}.{class_name}")
