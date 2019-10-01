from sklearn.externals import joblib
model = joblib.load('model.joblib')
print(model.predict([[0, 10, 10]]))