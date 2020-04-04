# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 11:19:49 2018

@author: ultrainstic
"""
#Crear la DB  con los nombres de los campos
https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/iris.data


"""
Crear un Login role y asignarselo ala DB 

new table iris owner usco2 (example)

column 

id = serial
xx = doublepresicion
name = charactervaring(100)

constrains->columns->id


"""

#Here goes all code. 
import pandas
import psycop2


# How to get pandas data from postgres sql using python

import psycopg2 as pg
import pandas as pd
connection = pg.connect("host='127.0.0.1' dbname=usco2 user=usco2 password='usco2'")
df = pd.read_sql_query("select * from iris where class = 'Iris-versicolor'", con=connection)

print(df)

df.to_cvs("uno.cvs")

archivo = 
df.to_hdf(archivo)

connection.close()



dtframe a h5py