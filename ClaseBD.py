# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 11:19:49 2018

@author: ultrainstic
"""
#Crear la DB  con los nombres de los campos
# https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/iris.data


"""
Crear un Login role y asignarselo ala DB 

new table iris owner usco2 (example)

column 

id = serial
xx = doublepresicion
name = charactervaring(100)

constrains->columns->id

Accesar a una base datos de postgrest desde python
"""

#Here goes all code. 
import pandas
import psycopg2


# Connect to an existing database
conn = psycopg2.connect(dbname="usco2", user="usco2", password="usco2")

# Open a cursor to perform database operations, Posicion para los registros. 
cur = conn.cursor()


url = "https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/iris.data"
df = pandas.read_csv(url)

for index, row in df.iterrows():
    sl = row['SepalLength']
    sw = row['SepalWidth']
    pl = row['PetalLength']
    pw = row['PetalWidth']
    sp = row['Name']
    print(sl,sp)
    
    campos = "sepal_length, sepal_width, petal_length, petal_width, class"
    
    cur.execute("INSERT INTO iris (" + campos + ") Values (%s, %s, %s, %s, %s)",
                (sl, sw, pl, pw, sp))
    

conn.commit()



import psycopg2 as pg
import pandas as pd
connection = pg.connect("host='127.0.0.1' dbname=usco2 user=usco2 password='usco2'")
df2 = pd.read_sql_query('select * from iris' ,con=connection)
    
    
df2['class'].unique() 
df2['sepal_length'].min()
df2['sepal_length'].max()
df2['sepal_length'].mean()
df2['sepal_length'].std()
df2['sepal_length'].count()

df3 = df2.query('sepal_length>7')
df4 = df2.query('sepal_length<5')
df5 = pandas.concat([df3, df4])





# Un sistema inteligente , con plataforma, So, ZP = python windos, .. Modelo de caldificacion, 
# Teniendo en cueneta los paramtros que hemos trabajdo, a que calse perteneces
# 
















    