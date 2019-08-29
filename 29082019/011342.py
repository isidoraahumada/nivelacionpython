import numpy as np 

a = np.array([3,-1,-2,4,-6,8]) #crea un arreglo a 


#EJ: imprimir numeros negativos del arreglo a con mask 
negativos = a < 0 #identifica los elementos negativos 
print a[negativos] #imprime los elementos negativos 
print a[a<0] #otra forma de imprimir los numeros negativos del arreglo 

a[a<0] = 0 #reemplazo los numeros de a que son menores a cero por cero 
print a

print (a < 8).any () #imprime si esq algun elemento es menor a 8 (True)
print (a>3) & (a<8) 

a.sort () #ordena los elementos del arreglo de menor a mayor 
print a

a = np.array ([10,2,20])
b = np.array ([2,3,20])
print a>b #imprime true o false, dependiendo si se cumple la condicion entre cada par de elemntos 

c = np.array([10, 1, 20])
subset = c[[0, 2]] #agrega el primer y tercer elemento del arreglo c a un nuevo arreglo subset
print subset
#[10 20]
subset[0]=-1 #cambia el primer elemento de subset por -1 
print subset

