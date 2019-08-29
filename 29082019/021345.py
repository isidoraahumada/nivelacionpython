import numpy as np 

a = np.arange(24).reshape(6,4) #crea una matriz con numeros del 0 al 23, con 6 filas y 4 columnas 
print a.shape #muestra las filas y columnas de la matriz (6,4)
print a #muestra la matriz 
print a.mean(axis=0).shape #imprime el promedio de los elementos del eje 0 