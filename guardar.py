# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 12:27:36 2018

@author: Mr Mejia
"""

import request
import json
body = {"sl":5.2, "sw":3.4, "pl":1.4, "pw":0.2}
r = request.post('http://localhost:5000/classify', json=body)
print(r.headers)
print(type(r.text))
print(r.text)


data = json.data(r.text)
clase = data['clase']
print(clase)



