WIP


Minimal example (SVC):

````python
from sklearn.svm import SVC
from scikit_learn_json import Serializer

# train model
x = [[0, 0], [1, 1]]
y = [0, 1]
model = SVC()
model.fit(x, y)

# save to json
serializer = Serializer()
serializer.serialize(model, "model.json")

# load from json
loaded_model = serializer.deserialize("model.json")

````
