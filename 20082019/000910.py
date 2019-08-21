# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:30:23 2019

@author: Isi
"""

#con dos arguemntos 
def function3(x,y):
    return x + y
    
a= function3 (1,2) #deberia ser 3
print a
    
def function4(x):
    print x
    print ("still in this function")
    return 3*x
    
b = function4(4) #al llamar a la funcion4 solo imprime lo que esta definido en la funcion para imprimir

print b #para que me imprima 12 (en este caso) debo pedirle q me lo imprima, ya que la funcion solo dice que imprima las dos primeras lineas y no el return

    
    