# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:36:06 2019

@author: Isi
"""

#ciclo for 

##EJEMPLO1
a = ["banana", "apple", "microsoft"]
#print a[0]
#print a[1]
#print a[2]

#si la lista tuviera mil elementos, no podriamos poner mil veces que imprima cada elemnto
for element in a: #ahora si tengo una lista de mil elementos si podria imprimir cada uno de ellos
    print element



##EJEMPLO2
b = [20,10,5] 
#para obtener la suma de los valores de la lista:
total=0
for e in b: 
    total = total + e 
    #primero total sera 0 por lo que sera 20 
    #a la siguiente vuelta el valor total nuevo sera 20 y se le suma 10 
    #por ultimo el total sera 30 y se le suma 5 
    #el valor final arrojara 35 
    #print total #este print me arrojara el valor de total en cada loop, es decir 20, 30 y 35
print total #el print lo pongo afuera del ciclo, ya que me interesa que se imprima el total final y no los de cada vuelta 



##EJEMPLO3
c=list(range(1,5)) #crea una lista sin incluir el numero de la izq, es decir muestra 1 2 3 4 
print c   

total2=0
for i in range (1,5):
    total2+= i #abreviacion de poner total2= total2 + i 

print total2
















