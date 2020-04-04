# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:08:30 2018

@author: Mr Mejia
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/clasificar/<float:sl>/<float:sw>')
def clasificar(sl, sw):
    suma = sl + sw
    return str(suma)

if __name__ == '__main__':
    app.run()