# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy import text
from pandas import DataFrame

class SensorPostgres:
    def getConnection(self):
        # Create connection
        engine = create_engine('postgres://sensor:sensor@localhost:5432/sensor')
        return engine
    
    
    def getDataFrame(self):
        # Execute query
        sql = text('select temperatura, humedad, clima from sensor')
        engine = self.getConnection()
        result = engine.execute(sql)
        # Convert sqlalchemy.engine.result to pandas dataframe
        dataframe = DataFrame(result.fetchall())
        dataframe.columns = result.keys()
        print(dataframe.head(5))
        return dataframe
    
        
        