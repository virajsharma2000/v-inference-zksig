import numpy as np
import json
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import skl2onnx

def main():
    iris = load_iris()
    X, y = iris.data.astype(np.float32), iris.target
    clf = DecisionTreeClassifier(max_depth=3)
    clf.fit(X, y)

    initial_types = [('input', skl2onnx.common.data_types.FloatTensorType([None, 4]))]
    onnx_model = skl2onnx.convert_sklearn(clf, initial_types=initial_types)
    with open("iris_model.onnx", "wb") as f:
        f.write(onnx_model.SerializeToString())

    # Save one sample input for witness generation
    payload = {"input": X[0].tolist()}
    with open("input.json", "w") as f:
        json.dump(payload, f)

    print("✅ Model exported to iris_model.onnx and input.json created.")

if __name__ == "__main__":
    main()
