from flask import Flask, request, jsonify
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__) 
model = joblib.load('model.joblib')

@app.route('/', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        data = request.get_json(force=True)
        prediction = model.predict(np.array([data['params']]).tolist()).tolist()
        output = prediction[0]
        return jsonify(output)
    else:
        return jsonify(err = 'Only POST allowed')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
