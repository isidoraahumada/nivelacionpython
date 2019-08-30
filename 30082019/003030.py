from matplotlib import pyplot as plt 

ages_x = [25,26,27,28,29,30,31,32,33,34,35] #lista de edades, en el eje x

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752] #saliarios, eje y 

#ahora para graficar esto:
plt.plot(ages_x, dev_y, color = "k",linestyle= "--",marker = ".",label = "all devs") #(ejex, eje y)


#py_dev_x = [25,26,27,28,29,30,31,32,33,34,35] #como es igual a dev_x, esta linea de codigo se puede borrar
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640] #eje y pero otra linea 
#para graficar:
plt.plot (ages_x,py_dev_y, color = "b", linewidth = 3,marker = "o",label="python")


js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583] #eje y para otra linea 
#para graficar
plt.plot (ages_x, js_dev_y, color = "#adad3b", linewidth = 3, marker = "o",label="javascript")


plt.xlabel ("edades") #titulo eje x
plt.ylabel ("median salary (USD)") #titulo eje y
plt.title("median salary (USD) por edad") #titulo del grafico
#plt.legend(["all devs", "python"]) #le da un nombre a las lineas del grafico , pero hay que acordarse de el orden en q fueron puestas por lo que se puede hacer de otra forma 

plt.legend() #para que lea el label de los eje y 
plt.grid (True) #pone cuadraditos de las coordenadas en el grafico 
plt.tight_layout()
plt.savefig("plot.png") #guarda la imagen en la carpeta 
plt.show() #muestra el grafico 