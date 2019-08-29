import numpy as np 

a = np.array ([1,2,3,4]) #crea un arreglo de int (numero enteros)
a = np.array ([1,2,3,4.0]) #crea un arreglo de float (decimales), debido a q se pone un elemnto con decimales por lo que el arreglo se convierte en uno de decimales
print a #muestra el arreglo a en float
print a.dtype #muestra que el arreglo a esta en float (decimales)

a = np.array ([1,2,3,4.0], dtype= 'int32') #el dtype define que el arreglo estara en int (numero enteros)
print a #muestra el arreglo a en int
print a.dtype #muestra que el arreglo a ahora esta en int 
#si no pongo el dtype = "float, int, etc" el programa lo dara por default dependiendo si el arreglo lo escribo en numeros enteros o decimales

c = np.array ([[10,11,12], [20,21,22]]) #lista dentro de una lista, en un arreglo. Seria como una matriz
print c #muestra el arreglo c como una matriz
print c.dtype #muestra q el arreglo c esta en int 
print c.ndim #muestra q el arreglo c tiene 2 dimensiones
print c.shape #muestra que el arreglo tiene 2 elementos en la primera dimension y 3 en la segunda, es decir 2 filas y 3 columnas 
print c.size #imprime la cantidad de elementos del arreglo 
print c.nbytes #la memoria que se esta usando 


print a[0] #imprime el primer elemnto del arreglo 
print a[2] #imprime el tercer elemento del arreglo 

print c[0][0] #imprimre el primer elemento de la primera fila o primer arreglo 
print c[0][1] #imprime el segundo elemnto de la primera fila o primer arreglo



