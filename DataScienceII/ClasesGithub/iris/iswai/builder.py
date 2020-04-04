# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 14:33:12 2019

@author: Mr Mejia
"""

from flask import Flask, jsonify
from iswai.iris_mongodb import IrisMongoDB
from sklearn import model_selection
from sklearn.svm import SVC
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/build')
def build_model():
    # Load Dataset
    iris_mongodb = IrisMongoDB()
    dataset = iris_mongodb.getDataframe()
    
    # Split-out validation dataset
    array = dataset.values
    X = array[:,1:5]
    Y = array[:,0]
    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(
            X, Y, test_size = validation_size, random_state=seed)
    
    # Make predictions on validation dataset
    model = SVC()
    model.fit(X_train, Y_train)
    
    # Save the iris classification model
    joblib.dump(model, 'models/iris_svc.model')
    
    return jsonify({'response': 'Iris SVC model saved'})

if __name__ == '__main__':
    app.run()
    
    
    
    
    
    
        