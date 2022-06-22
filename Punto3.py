import numpy as np

#Se recibe por consola la secuencia de numeros por ejemplo 3,4,5,6,4,3
numeros=input()
#Especifico el separador de los numeros y creo la lista con ellos
numerosString=numeros.split(",")
#Convierto la lista a una lista de numeros enteros
numerosEnteros=list(map(int,numerosString))
#Convertimos la lista en un array de numpy para aprovechar las funciones que la libreria nos ofrece
numerosEnterosNp=np.array(numerosEnteros)
#Retorna la lista de menor a mayor ayudandonos de la funcion "sort" que la libreria de numnpy nos ofrece
#Cabe aclarar que si quisieramos cambiar el orden de mayor a menor deberiamos agregar el parametro "reverse=true"
print(np.sort(numerosEnterosNp))