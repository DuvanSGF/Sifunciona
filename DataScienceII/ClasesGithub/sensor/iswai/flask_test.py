# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from iswai.sensor_mongodb import SensorMongoDB
from iswai.sensor_postgres import SensorPostgres

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = {'id':123, 'name':'Flask test' }
    return jsonify(message)


@app.route('/mongodb')
def mongodb():
    sensor_mongodb = SensorMongoDB()
    dataframe = sensor_mongodb.getDataframe()
    data_json = dataframe.to_json(orient='records')
    return jsonify(data_json)


@app.route('/postgres')
def postgres():
    sensor_postgres = SensorPostgres()
    dataframe = sensor_postgres.getDataFrame()
    data_json = dataframe.to_json(orient='records')
    return jsonify(data_json)


if __name__ == '__main__':
    app.run()

    