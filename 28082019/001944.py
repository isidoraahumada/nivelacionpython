import numpy as np 

a = np.arange(10) #crea un arreglo con elementos del 0 al 10 

np.random.shuffle(a) #desordena el arreglo y arroja los numeros del 0 al 10 pero no en orden 
print a

numero_al_azar=np.random.choice(a)
print numero_al_azar #arroja un numero al azar del arreglo a, es decir un numero entre 0 y 10 

b = np.random.random_integers (5,10,2) #arroja un arreglo de dos numeros entre el 5 y el 10 
print b
