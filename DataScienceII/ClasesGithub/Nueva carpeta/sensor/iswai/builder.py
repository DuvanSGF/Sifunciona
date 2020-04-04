# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 18:15:25 2019

@author: Mr Mejia
"""
from flask import Flask, jsonify
from iswai.sensor_mongodb import SensorMongoDB
from sklearn import model_selection
from sklearn.svm import SVC
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/build')
def build_model():
    # Load Dataset
    sensor_mongodb = SensorMongoDB()
    dataset = sensor_mongodb.getDataframe()
    
    # Split-out validation dataset
    array = dataset.values
    X = array[:,1:3]
    Y = array[:,0]
    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(
            X, Y, test_size = validation_size, random_state=seed)
    
    # Make predictions on validation dataset
    model = SVC()
    model.fit(X_train, Y_train)
    
    # Save the iris classification model
    joblib.dump(model, 'models/sensor_svc.model')
    
    return jsonify({'response': 'Sensor SVC model saved'})

if __name__ == '__main__':
    app.run()
