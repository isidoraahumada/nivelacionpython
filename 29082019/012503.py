import numpy as np 

a = np.arange (25).reshape(5,5) #crea una matriz con elementos del 0 al 24 con 5 filas y 5 columnas 
print a
 
print a%3 #muestra el resto de la division por 3 de cada elemento 
print a % 3 ==0 #muestra si es verdad o falso que el resto de a/3 es cero, para cada elemento 
print a[a % 3 ==0] #imprime los q salieron true, en una dimension



