# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:54:58 2019

@author: Isi
"""

#while loops
#el while se usa situaciones como por ejemplo cuando no sabes cuantos loops necesitas 
#en este caso es mejor usar while que loops (ciclo for) 

##EJEMPLO 1
total2=0
j=1
while j <5: #sumara los digitos hasta que el j sea menor a 5, es decir del 1 al 4
    total2 += j
    j+=1 #la variable j va tomando el valor de 1, 2, 3, 4 , 5.....
print "total2 =", total2 



##EJEMPLO 2
given_list = [5,4,4,3,1,-2,-3,-5]#necesitamos la suma de solo los numeros positivos de esta lista 
total3 =0
i=0 #identificara la posicion del elemento en la lista 
while given_list[i] >0: #mientras cada elemento i de la givenlist sea mayor a cero 
    total3 += given_list[i] #si ocurre que es mayor a 0, se sumara al total
    i +=1 #para q la variable i avance 

print "total3 =", total3    



##EJEMPLO 2 MEJORADO para que no haya error cuando termine de leer la lista 
given_list1=[5,4,4,3,1]
total4 =0
l=0 #identificara la posicion del elemento en la lista 
while l < len(given_list1) and given_list1[l] >0: #se agrega que i sea menor a len, len cuenta los items de la lista  
    total4 += given_list1[l] #si ocurre que es mayor a 0, se sumara al total
    l +=1 #para q la variable i avance 

print "total4 =", total4 


  
  