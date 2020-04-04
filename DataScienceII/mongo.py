# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 12:14:02 2018
Hay que empezar la db de mongo y el usuario, y entrar en la db iris
Insertando datos con python a mongoBD
@author: Mr Mejia
"""

from pymongo import MongoClient
client = MongoClient()

"""
 mongo ds011913.mlab.com:11913/irisdb -u administrador -p admin12345
"""
#client = MongoClient ('mongodb:// ds011913.mlab.com:11913/irisdb -u administrador -p admin12345

db = client['iris']
collection = db['especies']

data = {"sl":5.1,"sw":3.5,"pl":1.4,"pw":0.2,"class":"Iris-setosa"}
especie_id = collection.insert_one(data).inserted_id
print(especie_id)

print(collection.find_one())
print(type(data))
print(data)

clase = data['class']
pl = data['pl']

print(clase)
print(pl)

data = collection.find_one({},{"_id":0, "class":1})
print(type(data))
print(data)

cursor = collection.find()
for doc in cursor:
    print(doc)
    print(doc['class'])