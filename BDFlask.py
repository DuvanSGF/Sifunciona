# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:50:21 2018

@author: Mr Mejia
"""
from flask import Flask, request, jsonify
import psycopg2 as pg
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

def get_connection():
    connection = pg.connect("host='127.0.0.1' dbname=usco2 user=usco2 password='usco2'")
    return connection


def get_dataset():
    connection = get_connection()
    sql = "SELECT sepal_length, sepal_width, petal_length, petal_width, class FROM iris"
    dataset = pd.read_sql_query(sql, con=connection)
    
    return dataset

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/build')
def build():
# Check the versions of libraries

# Python version
    import sys
    print('Python: {}'.format(sys.version))
# scipy
    import scipy
    print('scipy: {}'.format(scipy.__version__))
# numpy
    import numpy
    print('numpy: {}'.format(numpy.__version__))
# matplotlib
    import matplotlib
    print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
    import pandas
    print('pandas: {}'.format(pandas.__version__))
# scikit-learn
    import sklearn
    print('sklearn: {}'.format(sklearn.__version__))
    
    # Load libraries
    import pandas
    from pandas.plotting import scatter_matrix
    import matplotlib.pyplot as plt
    from sklearn import model_selection
    from sklearn.metrics import classification_report
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    
    # Load dataset
    """
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = pandas.read_csv(url, names=names)
    """
    dataset = get_dataset()
    # shape
    print(dataset.shape)
    
    # head
    print(dataset.head(150))
    
    # descriptions
    print(dataset.describe())
    # class distribution
    print(dataset.groupby('class').size())
 
        # Split-out validation dataset
    array = dataset.values
    X = array[:,0:4]
    Y = array[:,4]
    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
    

    
        # Make predictions on validation dataset
    knn = KNeighborsClassifier()
    knn.fit(X_train, Y_train)
    
    #Guarda el modelo en la Clasificacion
    filehander = open("C:Ingenieria_Software\DataScience\knn.model","wb")
    pickle.dump(knn,filehander)
    filehander.close()
    
    return 'model finished!'

@app.route('/classify', methods=['POST'])
def classify():
    file = open("C:Ingenieria_Software\DataScience\knn.model", 'rb')
    knn = pickle.load(file)
    file.close()
    
    json_data = request.json
    
    sl = 4.4
    sw = 2.9
    pl = 1.4
    pw = 0.2
    datos = np.array([sl, sw, pl, pw], ndadmin = 2)
    
    predictions = knn.predict(datos)
    
    print (type(predictions))
    return jsonify(clase=predictions[0])

    return 'algo!'
if __name__ == '__main__':
    app.run()