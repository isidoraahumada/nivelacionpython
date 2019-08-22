# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:16:48 2019

@author: Isi
"""

#EJEMPLO4 

#el signo % da el resto de la division 
#4%3 arrojara 1 
#10%3 arrojara 1
#12%3 arrojara 0 

#entonces si ahora se quieren sumar solo los multiplos de 3 de un arreglo del 1 al 8 sera
total3= 0 
for i in range(1,8):
    if i%3 == 0: #si esto se cumple
        total3+= i #se sumara al total 
print total3 #arroja 9, ya que los unicos multiplos del 1 al 8 es 3 y 6 

       