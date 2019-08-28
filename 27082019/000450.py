import numpy as np 

#ARREGLOS (son como matrices)
#introduccion a los arreglos, codigos claves 

a = np.zeros (3) #imprime un arreglo de 3 ceros floats (con decimales)
print a

z= np.zeros (10) #arreglo de 10 ceros floats (con decimales)
print z

z.shape = (10,1) #ya no es una fila de ceros, si no que una columna 
print z

z = np.ones (10) #arreglo de unos 
print z 

z = np.empty (3) #crea un arreglo vacio para luego rellenarlo 

z = np.linspace (2,10,5) #from 2 to 10, with 5 elements. Parte del 2 al 10, con 5 elemntos 
print z

z = np.array ([10,20]) #crea un arreglo con los elemntos entre []
print z

a_list = [1,2,3,4,5,6,7] #lista
z = np.array ([a_list]) #pasa los elemntos de la lista a un arreglo guardado en la variable z
print z

b_list = [[9,8,7,6,5,4,3],[1,2,3,4,5,6,7]]
x = np.array([b_list]) #crea una matriz con las listas anteriores, teniendo dos filas y siete columnas 
print x

x1 = np.random.randint (10,size = 6) #crea un arreglo aleatorio entre 0 y 9 de 6 numeros 
print x1

print x1[0] #imrpime el primer elemento del arreglo x1 
print x1[2] #imprime el tercer elemento del arreglo x1 
print x1[0:2] #imprime los dos primeros elementos del arreglo x1
print x1[0:3] #imprime del elemnto 1 al 3 del arreglo x1 
