# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:17:40 2019

@author: Isi
"""

#EJERCICIO 
#sumar solo los numeros negativos de la lista 
lista = [7,5,4,3,1,-2,-3,-5,-7]

total3 =0
i=-1 #para que parta recorriendo la lista de atras para adelante 
#parte con una verdad
while lista[i] < 0 and i < len(lista): #mientras cada elemento i de la lista sea menor a cero (partiendo de izq a derecha)
    total3 += lista[i] #si ocurre que es menor a 0, se sumara al total
    i -=1 #para q la variable i avance 

print "total3 =", total3 




##al principio lo habia hecho partiendo el i=0, asi recorria la lista de derecha a izquierda 
#i=0 
#while lista [i] < 0:
    #total3+= lista [i]
    #i-= 1
## me arrojaba cero, ya que partia con algo que no es verdadero 
## diciendo que el primer elemento de la lista era menor a cero, lo cual no es verdad
