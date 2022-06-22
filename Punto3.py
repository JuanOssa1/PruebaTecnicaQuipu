import numpy as np

numeros=input()
numerosString=numeros.split(",")
numerosEnteros=list(map(int,numerosString))
numerosEnterosNp=np.array(numerosEnteros)

print(np.sort(numerosEnterosNp))