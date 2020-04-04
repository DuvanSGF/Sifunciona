# -*- coding: utf-8 -*-

#Here goes all code. 
import pandas
import psycopg2


# Connect to an existing database
conn = psycopg2.connect(dbname="iris", user="iris", password="iris")

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
    #print(sl,sp)
    
    campos = "sepal_length, sepal_width, petal_length, petal_width, category"
    
    cur.execute("INSERT INTO iris (" + campos + ") Values (%s, %s, %s, %s, %s)",
                (sl, sw, pl, pw, sp))
    

conn.commit()