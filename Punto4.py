import numpy as np
from pyparsing import counted_array

#Inicializamos la variable contador que nos ayudara a llevar la cuenta de los numeros repetidos
counter=0
#Inicializamos el diccionario donde estaran los elementos repetidos y las veces que se repiten
dictionaryOfRepeatedElements={}
#Se recibe por consola la secuencia de numeros por ejemplo 3,4,5,6,4,3
numeros=input()
#Especifico el separador de los numeros y creo la lista con ellos
numerosString=numeros.split(",")
#Convierto la lista a una lista de numeros enteros
numerosEnteros=list(map(int,numerosString))
#Convertimos la lista en un array de numpy para aprovechar las funciones que la libreria nos ofrece
numerosEnterosNp=np.array(numerosEnteros)
#Ordena el arreglo de menor a mayor ayudandonos de la funcion "sort" que la libreria de numnpy nos ofrece
#Para que de aqui en adelante las demas listas que se creen ya esten ordenadas
numerosEnterosNpSorted=np.sort(numerosEnterosNp)
#Hacemos uso de la funcion "unique" que sacara un arreglo con cada uno de los elementos de la lista inicial pero sin que estos esten repetidos
listaDeNumerosUnicos=np.unique(numerosEnterosNpSorted)

#El for externo estara recorriendo la lista con los elementos que no estan repetidos, y sumara al contador 1 cada que encuentre
#un elemento igual a el, como la lista inicial con elementos repetidos esta ordenada, inmediatamente cuando encuentre otro numero diferente a la del for 
#externo dejara de sumar al contador y guardara el valor del for externo que es el numero que esta contando que se repite y el contador 
# que indica cuantas veces se repite ese numero, ya que cuando sucede esto significa que ese numero no se repite mas y seguira con el otro hasta que
# termine con el arreglo de los numeros unicos. 
for x in listaDeNumerosUnicos:
    for y in numerosEnterosNpSorted:
        if(x==y):
            counter+=1
    #Imprime la informacion de una manera mas legible
    print("Elemeto a contar: ", x, "Numero de veces repetidas: ",counter)
    dictionaryOfRepeatedElements[x]=counter
    counter=0
#Imprime el diccionario que ha sido lo que se ha solicitado
print("Diccionario: ",dictionaryOfRepeatedElements)


    

