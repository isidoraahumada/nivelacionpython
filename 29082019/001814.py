import numpy as np 

a = np.array ([1,2,3,4]) #crea un arreglo 
b = np.array ([10,11,12,13]) #crea otro arreglo 
print a.ndim #da la dimension de mi arreglo, en este caso sera 1 
print a.shape #retorna el numero de elementos en cada dimension, en este caso 4 

print a * b #multiplica cada elemento del arreglo a por el elemnto del arreglo b
print a * 10 #multiplica cada elemento de a por 10 
print a * 100 #multiplica cada elemento de a por 100 

print np.sin(a) #imprime el seno de cada elemento de a 
print np.exp (a) #imprime la funcion exponencial para cada elemento de a
print np.log(a) #imprime el log de cada elemento de a
#explica que estas funciones son muy simples y comodas de aplicar para la libreria numpy, ventaja por sobre las listas 







