# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:29:50 2019

@author: Isi
"""

#este es un ejemplo donde utiliza los bloques if y else, para definir si una persona tiene sobrepeso o no 


name = "isidora"
height_m = 2
weight_kg = 90

bmi = weight_kg/ (height_m **2)
print ("bmi: ")
print bmi
if bmi < 25:
    print name
    print ("is not overweight")
else: 
    print name 
    print ("is overweight ")