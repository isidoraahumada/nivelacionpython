# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:11:45 2019

@author: Isi
"""

#functions

def function1(): #nombre de la funcion 
    print ("hola")
    print ("holaaaaa") #hasta aqui esta dentro de la funcion1
print ("this is outside the function")    

function1() #para que se imprima el hola y holaaaa se debe llamar a la funcion 



def function2(x): #la variable x se transforma en el numero q pongamos entre () cuando llamemos a la funcion
    return 2*x 
    
a= function2(3) #el resultado de esta funcion se le asociara a la letra a
print a

b=function2(10) #arrojara 20 
print b

  
    