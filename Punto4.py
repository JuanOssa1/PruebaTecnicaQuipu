import numpy as np
from pyparsing import counted_array

counter=0
dictionaryOfRepeatedElements={}
numeros=input()
numerosString=numeros.split(",")
numerosEnteros=list(map(int,numerosString))
numerosEnterosNp=np.array(numerosEnteros)
numerosEnterosNpSorted=np.sort(numerosEnterosNp)
listaDeNumerosUnicos=np.unique(numerosEnterosNpSorted)

for x in listaDeNumerosUnicos:
    for y in numerosEnterosNpSorted:
        if(x==y):
            counter+=1
    print("Elemeto a contar: ", x, "Numero de veces repetidas: ",counter)
    dictionaryOfRepeatedElements[x]=counter
    counter=0

print("Diccionario: ",dictionaryOfRepeatedElements)


    

