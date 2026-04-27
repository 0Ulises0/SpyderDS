# -*- coding: utf-8 -*-

### EL OBJETIVO DE REGRESION LINEAL ES MINIMIZAR LA VERTICAL ENTRE TODOS LOS DATOS Y NUESTRA LINEA QUE VENDRIA SIENDO EL MODELO, POR LO TANTO
### PARA DETERMINAR LA MEJOR LINEA, DEBEMOS MINIMIZAR LA DISTANCIA ENTRE TODOS LOS PUNTOS Y LA DISTANCIA DE NUESTRA LINEA

#%% LinearRegression

from sklearn import linear_model

x_train = varX_train
y_train = varY_train
x_test = varX_test
y_test = varY_test

# Definir el algoritmo
algoritmo = linear_model.LinearRegression()

# Entrenar el modelo
algoritmo.fit(x_train, y_train)

# Predecir modelo
algoritmo.predict(x_test)

# Conocer el valor de la pendiente
a = algoritmo.coef_

#Conocer el valor de la interseccion
b = algoritmo.intercept_

# Conocer la presicion del modelo
precision = algoritmo.score(x_test, y_test)