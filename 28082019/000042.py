#LIBRERIA NUMPY
#ventajas de los arreglos vs las listas 

import numpy as np 

#LISTAS
lista = [0,1,2,3]
for i in range (len(lista)): #debo hacer un loop para multiplicar cada elemento de la lista x 3
	lista[i] *=3
print lista 

#ARREGLOS 
arreglo = np.array ([0,1,2,3]) #el codigo para realizar lo mismo que antes es mas corto, mas eficiente
arreglo *=3
print arreglo 



