# -*- coding: utf-8 -*-

# %% Gráfica de ejemplo y Matplotlib
import matplotlib.pyplot as plt

a = [1,2,3,4]
b = [11,22,33,44]

plt.plot(a,b, color='blue', linewidth=3, label='linea')
plt.legend()
plt.show()

#%%
a=[3,4,5,6]
b=[5,6,3,4]
plt.plot(a,b)
plt.show()