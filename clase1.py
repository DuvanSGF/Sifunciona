# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 10:18:52 2018
manejar con dataframe
@author: ultrainstic
"""
import csv
with open('eggs.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print ', '.join(row)

import csv
with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    
    
#Esto es para tomar un archivo de analisis de internet. 
import pandas
url = "https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt"
names = ["EDAD", "SEX", "BMI0", "BP", "S1","S2","S3","S4","S5","S6", "Y"]
df = pandas.read_csv(url, names=names, sep ='\t')
print (df.shape)
#Head
print(df.head(5))

#Para imprimirlo como un json
data = df.to_json(orient='records')
print(data)

#Para recorrelo dataframe
for index, row in df.iterrows():
    age = row['EDAD']
    bmi = row['BMI0']
    print(index, age, bmi)

