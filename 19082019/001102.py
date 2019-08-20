# -*- coding: utf-8 -*-
"""
@author: Isi
"""

#if - else
#el if se utiliza para poner condiciones, el else es como la otra opcion si esque else no se cumple
#el print outside the if block, lo usa para mostrarnos cuando sale de ese bloque if,
#es decir cuando el programa deja de pensar si c es menor que d o desde que linea 


#ejemplo cuando efectivamente c es menor a d (aplica if)
c=3
d=4
if c < d: 
    print ("c is less than d")
else:
    print ("c is NOT less than d")
    
print ("outside the if block")     
 

#ejemplo cuando d es menor a c (aplica else)  
c=5
d=4
if c < d: 
    print ("c is less than d")
else:
    print ("c is NOT less than d")
    
print ("outside the if block")      
