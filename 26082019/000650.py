#diccionarios en python 

#en los diccionarios se tiene las "keys" y los "values" que corresponden a pares

d= {} #diccionario vacio 

#d1 = {"George" : 24, "Tom" : 32} #george es la key y 24 es el value

d ["George"] = 24 #agrega el par key value al diccionario d
d ["Tom"] = 32 #agrega el par key value al diccionario d
d ["Jenny"] = 16 #agrega el par key value al diccionario d

print d["George"] #imprime el value de la key George, 24 en este caso 

#keys generalmente son strings (palabras) o numbers 
#se pueden mezclar los tipos de keys 
d[10] = 100 
print d[10]

#para mostrar los valores ordenados de un diccionario, mostrando su par key value respectivo 
for key, value in d.items ():
	print "key: ", key 
	print "value: ", value 
	print ""


