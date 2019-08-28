import numpy as np 
from skimage import io 

photo = io.imread ("hello.jpg") #convierte la foto en matriz 
print type (photo)
photo.shape #propiedades de la foto (filas, columnas)

import matplotlib.pyplot as plt 
plt.imshow(photo) #muestra la foto 

plt.imshow(photo[::-1]) #da vuelta la foto en 180 grados, queda como espejo, alreves

plt.imshow (photo[:,::-1]) #la foto queda con lo q estaba a la izq a la derecha y viceversa, pero no alreves, como q se cambian las cosas de lado 

plt.imshow(photo[50:150 , 150:280]) #muestra una parte de la foto, segun las coordenadas puestas 

plt.imshow(photo[::2,::2])

photo_sin = np.sin(photo) #entrega el seno de cada uno de los valores de la matriz photo 

z = np.array([1,2,3,4,5])
print z<3 #verifica si los valores del arreglo son menores a 3 
print z>3 #verifica si los valores del arreglo son mayores a 3 
print z[z>3] #imprime los valores del arreglo z que son mayores a 3

#asi es como se pueden editar las fotos
photo_editada = np.where(photo>100,255,0) #solo imprimira los valores de la foto que cumplan esa condicion, dandole asi un efecto ya que no imprime todos los colores o coordenadas de la matriz
plt.imshow(photo_editada)








