# -*- coding: utf-8 -*-

#%%
import matplotlib.pyplot as plt
import numpy as np


#%% DIAGRAMA DE LINEA
x1=[3,4,5,6]
y1=[5,6,3,4]
x2=[2,5,8]
y2=[3,4,3]

#Configurar las caracteristicas del grafico
plt.plot(x1,y1, label='Linea 1', linewidth=1, color='blue')
plt.plot(x2,y2, label='Linea 2', linewidth=4, color='green')

#Defiri titulo y nombres de ejes
plt.title('Diagrama de Lineas')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')


#Mostrar leyenda, cuadricula y figura
plt.legend()
plt.grid()
plt.show()

#%% DIAGRAMA DE BARRA
x1=np.arange(0.25, 5.25, 1)
y1=[10,55,80,32,40]
x2=np.arange(0.75, 5.75, 1)
y2=[42,26,10,29,66]
# Configurar las caracteristicas del grafico
plt.bar(x1,y1,label='Datos 1', width=0.5,color='lightblue')
plt.bar(x2,y2,label='Datos 2', width=0.5,color='orange')
# Definir el titulo y nombre de ejes
plt.title('Grafico de barras')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
# Mostrar leyenda y figura
plt.legend()
plt.show()

#%% HISTOGRAMAS
np.random.seed(0)
a = np.random.randint(0,120,32)
bins=np.linspace(0,100,11)
# Configurar las caracteristicas del grafico
plt.hist(a, bins, histtype='bar', rwidth=0.8, color='lightgreen')
# Definir el titulo y nombre de ejes
plt.title('Histogramas')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
# Mostrar figura
plt.show()

#%% GRAFICOS DE DISPERSION
x1=np.arange(0.25, 5.25, 1)
y1=[10,55,80,32,40]
x2=np.arange(0.75, 5.75, 1)
y2=[42,26,10,29,66]
#Configurar las caracteristicas del grafico
plt.scatter(x1, y1, label='Datos 1', color='green')
plt.scatter(x2, y2, label='Datos 2', color='purple')
# Definir el titulo y nombre de ejes
plt.title('Grafico de dispersion')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
# Mostrar leyenda y figura
plt.legend()
plt.show()

#%% GRAFICOS CIRCULAR
dormir = [7,8,6,11,7]
comer = [2,3,4,3,2]
trabajar = [7,8,7,2,2]
recreacion = [8,5,7,8,13]
divisiones =[7,2,2,13]
actividades = ['Dormir', 'Comer', 'Trabajar', 'Recreacion']
colores = ['red', 'purple', 'blue', 'orange']
#Configurar las caracteristicas del grafico
plt.pie(divisiones, labels=actividades, colors=colores, startangle=90,shadow=True, explode=(0.1,0,0,0), autopct='%1.1f%%')
# Definir el titulo y nombre de ejes
plt.title('Grafico circular')
# Mostrar figura
plt.show()
