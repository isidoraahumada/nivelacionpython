# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:23:29 2019

@author: Isi
"""

#EJERCICIO 

#Can you compute all multiples of 3,5 
#that are less than 100 

total=0
for i in range (1,100):
    if i % 3 == 0 or i % 5 == 0: #asi no se suma dos veces el numero que es multiplo de 3 y 5 
        total +=i
print total        
 
       
       