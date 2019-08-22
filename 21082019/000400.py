# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:38:12 2019

@author: Isi
"""

#listas

a = [3,10,-1]
print a

a.append (1) #agrego un 1 a la lista
a.append ("hello") #agrego una palabra a la lista 
a.append([1,2]) #agrego una lista dentro de la otra lista 
print a

a.pop() #borra el ultimo item de la lista 
print a
a.pop() #luego de ser actualizada de la lista, vuelve a borrar el ultimo item que quedo 
print a

print a[0] #te entrega el primer elemento de la lista, en este caso el 3

a[0]= 100 #ahora el primer item sera 100 y no 3 
a[1]=100 #el seegundo item tambien sera 100 y no 10 

print a #la lista final despues de todos estos cambios quedara con [100,100,-1,1]