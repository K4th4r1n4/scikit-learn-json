"""Test Serializer class."""

import pytest
import numpy as np
from sklearn.svm import SVC
from pathlib import Path

from scikit_learn_json.serializer import Serializer


@pytest.fixture()
def test_json_file():
    return Path("tests/test_model.json")


def test_serialize_svc():
    """Test (de)serialization of Support Vector Classifier."""
    # train model
    x = [[0, 0], [1, 1]]
    y = [0, 1]
    model = SVC()
    model.fit(x, y)

    # generate random test data
    x_test = np.random.randint(0, 2, size=(100, 2))

    # serialize
    serializer = Serializer()
    serialized_model = serializer._serialize_svc(model)
    model_parameter = serialized_model["model_parameter"]
    deserialized_model = serializer._deserialize_svc(model_parameter)

    # test prediction
    assert np.all(model.predict(x_test) == deserialized_model.predict(x_test))


def test_serialize_deserialize(test_json_file):
    """Test serialization and deserialization of an SVC."""
    # train model
    x = [[0, 0], [1, 1]]
    y = [0, 1]
    model = SVC()
    model.fit(x, y)

    # generate random test data
    x_test = np.random.randint(0, 2, size=(100, 2))

    # serialize
    serializer = Serializer()
    assert serializer.serialize(model, test_json_file)
    deserialized_model = serializer.deserialize(test_json_file)

    # test prediction
    assert np.all(model.predict(x_test) == deserialized_model.predict(x_test))

