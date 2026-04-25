# -*- coding: utf-8 -*-
#%%
import numpy as np
array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)
array

#%% Crear una matriz de unos
unos  = np.ones((3,4))
print(unos)

#%% Crear una matriz de ceros
ceros = np.zeros((3,4))
print(ceros)

#%% Crear una matriz con numeros aleatorios
aleatorios = np.random.random((2,2))
print(aleatorios)

#%% Crear una matriz vacia
vacia = np.empty((3,2))
print(vacia)

#%% Crear una matriz llena con un valor
full = np.full((2,2), 8)
print(full)

#%% Crear una matriz con valores espaciados uniformemente
espacio1 = np.arange(0,30,5)
espacio2 = np.linspace(0, 2, 5)
print(espacio1)
print(espacio2)

#%% Crear una matriz identidad
identidad1 = np.eye(4,4)
identidad2 = np.identity(4)
print(identidad1)
print(identidad2)


###########ATRIBUTOS DE LAS MATRICES############################

#%% Conocer las dimensiones de una matriz
a = np.array([(1,2,3), (4,5,6)])
print(a.ndim)
print(a.dtype)
print(a.size)
print(a.shape)

#%% Cambio de forma de una matriz
a = np.array([(8,9,10), (11,12,13)]) # 2x3
print(a)
a = a.reshape(3,2) #3x2
print(a)


###########INDEXAMIENTO DE LAS MATRICES############################

#%% Extraer un solo valor de la matriz - el valor ubicado en la fila 0 columna 2
a = np.array([(1,2,3,4), (3,4,5,6)])
print(a[0,2])

#%% Extraer los valores de todas las filas ubicados en la columna 3
a = np.array([(1,2,3,4), (3,4,5,6)])
print(a[0:,2])



###########OPERACIONES MATEMATICAS DE LAS MATRICES############################
#%% Encontrar el minimo, maximo y la suma
a = np.array([2,4,8])
print(a.min())
print(a.max())
print(a.sum())

#%% Calcular la raiz cuadrada y la desviacion estandar
a = np.array([[1,2,3], [3,4,5]])
print(np.sqrt(a))
print(np.std(a))

#%% Calcular la suma, resta, multiplicacion y division de dos matrices
x = np.array([[1,2,3], [3,4,5]])
y = np.array([[1,2,3], [3,4,5]])
print(x+y)
print(x-y)
print(x*y)
print(x/y)