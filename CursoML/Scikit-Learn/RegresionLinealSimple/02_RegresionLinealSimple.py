# -*- coding: utf-8 -*-

#%%
import numpy as np
from sklearn import datasets, linear_model
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import pandas as pd

#%%
boston = pd.read_csv('Scikit-Learn/RegresionLinealSimple/BostonHousing.csv')
boston.keys()

#%% Seleccionar UNA VARIABLE INDEPRENDIENTE, en este caso sera RM
X = boston[['rm']]
y = boston['medv']

#%% Graficar para ver si hay correlacion
plt.scatter(X,y)
plt.xlabel('Media de Habitaciones')
plt.ylabel('Precio medio')
plt.show()

#%% Separar los datos en entrenamiento y prueba
from sklearn.model_selection import train_test_split

#Separar los datos (20% para pruebas)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

#%% Seleccionar el modelo
lr = linear_model.LinearRegression()
lr.fit(X_train, y_train)

Y_pred = lr.predict(X_test)

#%% Graficar el modelo junto con los datos
plt.scatter(X_test, y_test)
plt.plot(X_test, Y_pred, color='red', linewidth=2)
plt.title('Regresion Lineal Simple')
plt.xlabel('Numero de habitaciones')
plt.ylabel('Valor medio')
plt.show()

#%%
print('DATOS DEL MODELO')
print('Valor de la pendiente: ', lr.coef_)
print('Valor de la interseccion: ', lr.intercept_)
print(f'Ecuacion del modelo: y = {lr.coef_}x {lr.intercept_}')

#%% Precision del algoritmo
precision = lr.score(X_test, y_test)
precision