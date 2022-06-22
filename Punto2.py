import numpy as np

numeros=input()
numerosString=numeros.split(",")
numerosEnteros=list(map(int,numerosString))
numerosEnterosNp=np.array(numerosEnteros)
print("La suma de cada uno de los elementos al cuadrado es: ", np.sum((np.power(numerosEnterosNp,2))))