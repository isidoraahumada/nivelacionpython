# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:37:55 2019

@author: Isi
"""
#ejemplo calculadora bmi 

name1 = "isidora"
altura1 = 2
peso1 =90

name2= "josefa" 
altura2 = 1.8
peso2 = 70

name3= "paula"
altura3 = 2.5
peso3 = 160

def bmi_calculator (name, altura, peso):
    bmi = peso / (altura**2)
    print "bmi:", bmi
    if bmi < 25: 
        return name + " is not overweight"
    else: 
        return name + " is overweight"
        
result1= bmi_calculator(name1, altura1, peso1)  
result2= bmi_calculator(name2, altura2, peso2)
result3= bmi_calculator(name3, altura3, peso3)

#hasta aca solo me arrojara los valores de cada bmi 
#para que me muestre los nombres y si esque esta sobrepeso o no debo pedir que me lo imprima con un print 

print result1
print result2
print result3
