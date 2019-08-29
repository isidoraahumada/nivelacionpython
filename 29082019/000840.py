a = [1,2,3,4]
b = [10,11,12,13]
print a + b #agrega las dos listas a una, pero como en cadena una tras otra 

output = []
for item1, item2 in zip(a,b):
	output.append (item1 + item2) #suma los elementos de las listas, y los resultados los agrega a una nueva lista 
print output #[11,13,15,17]

import numpy as np 

g = list(range(1000000))
g_array = np.array(g) #la lista g se guarda como un arreglo 

#hace una comparacion del tiempo en que se demora en sumar los elementos de la lista g vs cuando se demora en sumar los elementos del arreglo g 
#para la lista se demora 7 seg por lopp y para el arreglo 4 seg, 
#por lo que demuestra y comprueba que usar los arreglos es mas eficiente 
