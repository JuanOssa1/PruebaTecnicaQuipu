import numpy as np

#Se recibe por consola la secuencia de numeros por ejemplo 3,4,5,6,4,3
numeros=input()
#Especifico el separador de los numeros y creo la lista con ellos
numerosString=numeros.split(",")
#Convierto la lista a una lista de numeros enteros
numerosEnteros=list(map(int,numerosString))
#Convertimos la lista en un array de numpy para aprovechar las funciones que la libreria nos ofrece
numerosEnterosNp=np.array(numerosEnteros)
#Se imprime un mensaje junto con la suma de los numeros al cuadrado ayudandonos de la funcion de "power" que eleva todo el arreglo al numero que le especifiquemos
#Y la funcion "sum" que suma cada uno de los elementos del arreglo
print("La suma de cada uno de los elementos al cuadrado es: ", np.sum((np.power(numerosEnterosNp,2))))