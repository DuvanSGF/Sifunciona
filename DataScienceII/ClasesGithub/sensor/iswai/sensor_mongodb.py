    # -*- coding: utf-8 -*-
from pymongo import MongoClient
import pandas as pd

class SensorMongoDB:
    def getCollection(self):
        client = MongoClient()
        db = client['sensor']
        collection = db['sensor']
        return collection
    
    def getDataframe(self):
        collection = self.getCollection()
        cursor = collection.find({},{'_id':0})
        dataframe = pd.DataFrame(list(cursor))
        print(dataframe.head(5))
        return dataframe
    