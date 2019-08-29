import numpy as np 
#indices de posicion 
# 0 1 2 3 4 
#-5 -4 -3 -2 -1 

#EJEMPLO
a = np.arange (25).reshape (5,5) #crea una matriz con numeros del 0 al 24 con 5 filas y 5 columnas
print a 

print a[0,3:5] #el cero indica la primera fila y el 3:5 indica las columnas de la 3 hasta la 4 (pq no incluye el 5)
print a[4:,4:] #4: se refiere a decir que imprima desde la cuarta (quinta en la matriz) posicion hasta el final 
print a[:,2] # : imprime la tercera columna de la matriz 

red = a[:,1::2] #los : son como decir una parte, una slice, de la matriz (no solo un elemento)
print red #imprime la segunda y cuarta columna de la matriz


print a[-1] #imprime la ultima fila de la matriz 
yellow = a[4] #otra forma de imprimr la ultima fila de la matriz 
print yellow 



