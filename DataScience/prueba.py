# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 11:47:43 2018

@author: ultrainstic
"""

#Esto es para tomar un archivo de analisis de internet. 
import pandas
url = "https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/iris.data"
names = ["SepalLenght","SepalWidth", "PetalLenght", "PetalWidt", "Name"]
df = pandas.read_csv(url, names=names, sep =',')
print (df.shape)
#Head
print(df.head(5))

data = df.to_json(orient='records')
print(data)

