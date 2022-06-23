import numpy as np
#Se recibe por consola la secuencia de numeros por ejemplo 3,4,5,6,4,3
print("Ingrese la secuencia de numeros enteros delimitada por comas: ")
numeros=input()
#Especifico el separador de los numeros y creo la lista con ellos
numerosString=numeros.split(",")
#Convierto la lista a una lista de numeros enteros
numerosEnteros=list(map(int,numerosString))
#Convertimos la lista en un array de numpy para aprovechar las funciones que la libreria nos ofrece
numerosEnterosNp=np.array(numerosEnteros)
#Se imprime un mensaje junto con el numero mas pequeño ayudandonos de la funcion "amin" de numpy que nos da el numero mas pequeño de la lista
#Cabe aclarar que tambien se ouede ordenar la lista de menor a mayor y coger el primer numero pero decidi hacer uso de "amin"
print("El elemento mas pequeño de la lista es: ", np.amin(numerosEnterosNp))
