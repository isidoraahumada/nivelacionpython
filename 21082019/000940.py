# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:06:54 2019

@author: Isi
"""

#ejemplo 

b = ["banana", "apple","microsoft"]

variable=b[0] #variable para guardar el primer termino aqui
b[0]=b[2] #aqui cambio el ultimo item al primero
b[2]=variable #y aqui cambio el primer item al ultimo

print b

##forma mas facil de hacer el cambio 

b[0],b[2] = b[2],b[0]
print b