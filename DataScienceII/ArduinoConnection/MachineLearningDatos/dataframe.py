# -*- coding: utf-8 -*-

import pandas
url = "https://raw.githubusercontent.com/DuvanSGF/Sifunciona/master/sensor.csv"
names = ["Temperatura","Humedad", "Clima"]
df = pandas.read_csv(url, names=names, sep =',')
print (df.shape)
#Head
print(df.head(5))

data = df.to_json(orient='records')
print(data)