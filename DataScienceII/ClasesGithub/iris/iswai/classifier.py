# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 15:04:40 2019

@author: Mr Mejia
"""
from flask import Flask, jsonify
from sklearn.externals import joblib
from iswai.iris_mongodb import IrisMongoDB

app = Flask(__name__)

@app.route('/classify/<float:pl>/<float:pw>/<float:sl>/<float:sw>')
def classify(pl, pw, sl, sw):
    
    # Load the saved iris classification  model
    model = joblib.load('models/iris_svc.model')
    
    # Make predictions on request data
    data = [pl, pw, sl, sw]
    predictions = model.predict([data])
    
    # return the classification in JSON format
    return jsonify({'class':predictions[0]})

@app.route('/classify', methods=['POST'])
def classify_json():
    # Load the saved iris classification model
    model = joblib.load('models/iris_svc.model')
    
    content = request.get_json()
    
    data = []
    for row in content:
        pl = row['pl']
        pw = row['pw']
        sl = row['sl']
        sw = row['sw']
        item = [pl, pw, sl, sw]
        data.append(item)
        
    # Make Predictions
    predictions = model.predict(data)
    
    # Return the classification in JSON format
    return jsonify(especies=predictions[0])


@app.route('/list', methods=['GET'])
def list():
    # Load the saved iris classification model
    model = joblib.load('models/iris_svc.model')
    
    iris_mongodb = IrisMongoDB()
    dataframe = iris_mongodb.getDataframe()
    print(dataframe)
    
    json_data = []
    
    for index, row in dataframe.iterrows():
        pl = row['petal_length']
        pw = row['petal_width']
        sl = row['sepal_length']
        sw = row['sepal_width']
        item = [pl, pw, sl, sw]
        
        category = model.predict([item])[0]
        json_item = {'pl':pl, 'pw':pw, 'sl':sl, 'sw':sw, 'class':category}
        json_data.append(json_item)
    
    return jsonify(flowers=json_data)

if __name__ == '__main__':
    app.run()
    
    

