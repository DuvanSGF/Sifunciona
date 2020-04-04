# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:53:18 2019

@author: Mr Mejia
"""



"""
-----------------------------------------------------------------------------
Crear la DB  con los nombres de los campos:
 https://raw.githubusercontent.com/DuvanSGF/Sifunciona/master/sensor1.csv
Crear un Login role y asignarselo ala DB 
-----------------------------------------------------------------------------

new table sensor owner sensor

column 

id = serial
xx = doublepresicion
name = charactervaring(100)

constrains->columns->id

Accesar a una base datos de postgres desde python
"""
import pandas
import psycopg2


# Connect to an existing database
conn = psycopg2.connect(dbname="sensor", user="sensor", password="sensor")

# Open a cursor to perform database operations, Posicion para los registros. 
cur = conn.cursor()


url = "https://raw.githubusercontent.com/DuvanSGF/Sifunciona/master/sensor1.csv"
df = pandas.read_csv(url)

for index, row in df.iterrows():
    tm = row['Temperatura']
    hm = row['Humedad']
    cl = row['Clima']

    #print(tm,hm)
    
    campos = "temperatura, humedad, clima"
    
    cur.execute("INSERT INTO sensor (" + campos + ") Values (%s, %s, %s)",
                (tm, hm, cl))
    

conn.commit()