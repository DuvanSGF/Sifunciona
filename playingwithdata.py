
# coding: utf-8

# In[2]:


# Importamos Pandas
import pandas as pd


# In[3]:


# Importamos pyplot
from matplotlib import pyplot as plt


# In[4]:


# Cargamos el dataset
url = "https://raw.githubusercontent.com/DuvanSGF/Sifunciona/master/sensor1.csv"


# In[5]:


# Leemos los datos
sample_data = pd.read_csv(url)


# In[6]:


# Imprimimos los datos 
sample_data


# In[7]:


type(sample_data)


# In[12]:


# Imprimimos la columna del Clima
sample_data.Clima


# In[13]:


# Tipo de valores de la columna Clima
type(sample_data.Clima)


# In[16]:


# Visualiza los datos de la columna clima dependiendo de la posicion 
sample_data.Clima.iloc[1]


# In[18]:


# Visualiza los datos de la columna Temperatura dependiendo de la posicion 
sample_data.Temperatura.iloc[1]


# In[27]:


# Temperatura vs Humedad
plt.plot(sample_data.Temperatura, sample_data.Humedad, 'o')
plt.show


# In[78]:


# Comparamos valores y analizamos
plt.plot(sample_data.Temperatura, 'o')
plt.plot(sample_data.Humedad, 'o')
plt.legend(['Temperatura', 'Humedad'])
plt.xlabel('Temperatura')
plt.ylabel('Humedad')
plt.show


# In[79]:


# Seleccionamos los datos solo Frio
frio = sample_data[sample_data.Clima == 'Frio']


# In[57]:


frio


# In[33]:


# Seleccionamos los datos solo Soleado
soleado = sample_data[sample_data.Clima == 'Soleado']


# In[83]:


# Comparamos
plt.plot(frio.Humedad)
plt.plot(frio.Temperatura)
plt.legend(['Humedad', 'Temperatura'])
plt.xlabel('Temperatura')
plt.ylabel('Humedad')
plt.show()


# In[77]:


frio.Humedad


# In[75]:


frio.Temperatura

