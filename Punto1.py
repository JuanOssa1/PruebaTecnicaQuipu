import numpy as np
#

numeros=input()
numerosString=numeros.split(",")
numerosEnteros=list(map(int,numerosString))
numerosEnterosNp=np.array(numerosEnteros)
print("El elemento mas pequeño de la lista es: ", np.amin(numerosEnterosNp))
