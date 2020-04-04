# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 18:15:39 2019

@author: Mr Mejia
"""

from flask import Flask, jsonify
from sklearn.externals import joblib
from iswai.sensor_mongodb import SensorMongoDB

app = Flask(__name__)

@app.route('/classify/<int:tm>/<int:hm>')
def classify(hm, tm):
    
    # Load the saved iris classification  model
    model = joblib.load('models/sensor_svc.model')
    
    # Make predictions on request data
    data = [hm, tm]
    predictions = model.predict([data])
    
    # return the classification in JSON format
    return jsonify({'clima':predictions[0]})

@app.route('/classify', methods=['POST'])
def classify_json():
    # Load the saved iris classification model
    model = joblib.load('models/sensor_svc.model')
    
    content = request.get_json()
    
    data = []
    for row in content:
        tm = row['tm']
        hm = row['hm']
        item = [tm, hm]
        data.append(item)
        
    # Make Predictions
    predictions = model.predict(data)
    
    # Return the classification in JSON format
    return jsonify(clima=predictions[0])


@app.route('/list', methods=['GET'])
def list():
    # Load the saved iris classification model
    model = joblib.load('models/sensor_svc.model')
    
    sensor_mongodb = SensorMongoDB()
    dataframe = sensor_mongodb.getDataframe()
    print(dataframe)
    
    json_data = []
    
    for index, row in dataframe.iterrows():
        tm = row['temperatura']
        hm = row['humedad']
        item = [tm, hm]
        
        category = model.predict([item])[0]
        json_item = {'tm':tm, 'hm':hm, 'clima':category}
        json_data.append(json_item)
    
    return jsonify(Tiempo=json_data)

if __name__ == '__main__':
    app.run()