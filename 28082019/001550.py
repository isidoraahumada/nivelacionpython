import numpy as np 
#principales codigos o comandos para los arreglos 

a = np.array ([2,3,4]) #crea un arreglo 
print a 

b = np.arange (1,12,2) #crea un arreglo del 1 al 12, cada dos numeros (inicio, fin, intervalo)
print b

c = np.linspace (1,12,6) #crea un arreglo con numeros del 1 al 12 con 6 elementos pero en float (decimales)
print c

c1=c.reshape (3,2) #cambia el arreglo c a una matriz de tres filas y dos columnas (filas, columnas)
print c1

print c.size #cantidad de elementos del arreglo
print c1.shape #cantidad de filas y columnas del arreglo o matriz 
print c.dtype #imprime la tipografia del arreglo (float, int, etc), y la memoria q usa en bytes

b = np.array ([(1,5,2,3), (4,5,6)]) #crea un array de dos dimensiones
print b

print c1<4 #verifica si cada valor del arreglo c1 son menores q 4, arrojando True or False
print c1*3 #multiplica cada valor del arreglo c1 x 3

d= np.zeros ((3,4)) #crea una matriz de ceros, con 3 filas y 4 columnas (fila, columna)
print d #es una matriz que le dicen vacia, para luego ir rellenando con numeros
print d.dtype #imprime la tipografia del arreglo (float, int, etc), y la memoria q usa en bytes

e=np.ones((2,3)) #crea una matriz de unos, 2 filas y 3 columnas 
print d 

f = np.array ([2,3,4], dtype = np.int16) #arreglo con 3 elementos, el dtype = 16 determina que use menos byte de memoria 
print f
print f.dtype #imprime la tipografia del arreglo (float, int, etc), y la memoria q usa en bytes

g = np.random.random((2,3)) #crea una matriz de 2 filas y 3 columnas con numeros aleatorios entre 0 y 1 (decimales)
np.set_printoptions(precision=2, suppress=True) #hace q los decimales de cada numero sean solo 2 
print g

h = np.random.randint (0,10,5) #crea un arreglo de 5 numeros del 0 al 10, aleatoriamente
print h #siempre va a salir distinto pq son numeros aleatorios 
print h.sum() #suma los valores del arreglo h 
print h.min () #muestra el numero mas chico del arreglo h 
print h.max () #muesrta el numero mayor del arreglo h 
print a.mean () #promedio de numeros del arreglo h 
print a.var() #varianza del arreglo h 

i = np.random.randint (1,10,6) #matriz con 6 elementos aleatorios del 1 al 10 
i = i.reshape (3,2) #ordena la matriz anterior en 3 filas y 2 columnas
print i
print i.sum(axis=1) #suma los elementos de la fila 
print i.sum(axis=0) #suma los elementos de la columna 
