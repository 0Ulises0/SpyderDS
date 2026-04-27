# -*- coding: utf-8 -*-

#%%
import pandas as pd
import numpy as np

data = np.array([['', 'Col1', 'Col2'], ['Fila1',11,22], ['Fila2',33,44]])
pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:])

#%%
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

#%% Se hace una matriz 3x3 directamente con numpy y se pasa a DataFrame
df = pd.DataFrame(np.array([[1,2,3], [4,5,6], [7,8,9]]))
df
#%%
series = pd.Series({'Argentina': 'Buenos Aires',
                    'Chile': 'Santiago de Chile',
                    'Colombia': 'Bogota',
                    'Peru': 'Lima'})
series

###EXPLORACION###

#%% Forma del Data Frame
df.shape
#%%Altura del Data Frame
len(df.index)

###Estadisticas###
print(df.describe())
print(series.describe())

#%%Media de las columnas del DataFrame
df.mean()

#%% Correlacion del DataFrame
df.corr()

#%% Cuenta los datos del DataFrame
df.count()

#%% Valor mas alto de cada columna del DataFrame
df.max()

#%% Valor minimo de cada columna del DataFrame
df.min()

#%% Mediana de cada columna del DataFrame
df.median()

#%% Desviacion estandar de cada columna del DataFrame
df.std()

###SELECCION###

#%% Seleccionar la primer columna del DataFrame
df[0]

#%% Seleccionar dos columnas del DataFrame
df[[0,1]]

#%% Seleccionar el valor de la primera fila y ultima columna del DataFrame POR SU POSICION
df.iloc[0][2]

#%% Seleccionar los valores de la primera dila del DataFrame por su INDICE
df.loc[0]

#%% Seleccionar los valores de la primera fila del DataFrame
df.iloc[0,:]


### IMPORTAR - EXPORTAR ###

#%% Importar CSV
df = pd.read_csv('Pandas/WA_Fn-UseC_-HR-Employee-Attrition.csv')
df.head()

#%% Exportar CSV
df.to_csv('Pandas/2.csv')

### LIMPIEZA ###

#%% Verificar si hay datos nulos en el DataFrame -> Retorna matriz booleana
df.isnull()

#%% Eliminar valores nulos
df.dropna()# ->Filas donde hay nulos
df.dropna(axis=1#) ->Columnas no de hay nulos
          
#%% Rellenar los valores nulos
df.fillna(df.mean())