# -*- coding: utf-8 -*-

# %% Gráfica de ejemplo con Seaborn y Matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generamos datos aleatorios (muy estilo tu libro de ISLP)
data = np.random.randn(1000)

# Configuramos el estilo de Seaborn
sns.set_theme(style="darkgrid")

# Creamos la gráfica
plt.figure(figsize=(8, 5))
sns.histplot(data, kde=True, color="skyblue")
plt.title("Distribución Normal en Spyder")

# En Spyder no siempre es obligatorio plt.show() si usas celdas,
# pero es buena práctica ponerlo.
plt.show()
