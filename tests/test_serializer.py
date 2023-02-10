"""Test Serializer class."""


import numpy as np
from sklearn.svm import SVC

from scikit_learn_json.serializer import Serializer


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
    serialized_model = serializer.serialize_svc(model)
    deserialized_model = serializer.deserialize_svc(serialized_model)

    # test prediction
    assert np.all(model.predict(x_test) == deserialized_model.predict(x_test))
