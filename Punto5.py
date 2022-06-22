from itertools import permutations
import requests as rq
import json

#ntrada por consola de la palabra a la que se le buscaran los anagramas
word=input()

#Esta funcion lo que hara es buscar en la Api publica de un diccionario en ingles una palabra y verufucara si existe
def searchWordInDictionary(word):
    #Definimos la URL y concatenamos la palabra que queremos buscar
    URL="https://api.dictionaryapi.dev/api/v2/entries/en/"+word
    #Obtenemos la respuesta de la API haciendo una solicitud "GET"
    response= rq.get(URL)

    #Dado que el estatus sea 200 (Que ha sido satisfactorio) lo que hara es convertir la respuesta en un string y luego en una lista
    #para poder sacar la informacion que nos sea util, este caso solo nos sirve el atributo "word" y retornara el valor de ese atributo
    if(response.status_code==200):
        dict=response.json()
        jsonString=json.dumps(dict)
        jsonInList= json.loads(jsonString)
        return jsonInList[0]['word'] 
    #Dado que no sea satisfactoria la respuesta significara que la palabra ingresada no existe y retornara un vacio  
    else:
        return ""

#Esta funcion hace uso de la funcion "permutation" de itertools que lo que hace es buscar todas las combinaciones posibles de una palabra,
#lo que se hara es que cada una de esas permutaciones la enviamos a la "searchWordInDictionary" que verificara si existe o no, si existe 
#la agrega al arreglo de anagramas que forma esa palabra y luego imprimera el arreglo con el conjunto de todos los anagramas
def createListOfWords(word):
    #Inicializamos la lista de anagramas vacia
    listOfAnagrams=[]
    #Se crea la lista con todas las permutaciones posibles
    listOfPermutations=permutations(word)
    #Recorre el arreglo con cada uno de los conjuntos de las permutaciones realizadas y les hace join que volveria formar la palabra 
    #de lo contrario imprimiria algo como ('c', 'a', 't') que al enviarlo a la api simplemente no encontraria nada
    for i in list(listOfPermutations):
        wordToValidate="".join(i)
        #Se imprime la permutacion que se esta validando en el momento
        print("Validando palabra: ", wordToValidate)
        #Se valida que si este retornando una palabra el metodo anterior, que como ya vimos retornara vacio si no encuentra nada
        if(len(searchWordInDictionary(wordToValidate))>=1):
            #Se agrega a la lista de anagramas encontrados la palabra que si entro en la condicion
            listOfAnagrams.append(searchWordInDictionary(wordToValidate))
    #Luego quen termina de mirar todas las permutaciones imprime la lista final con todos los anagramas encontrados 
    print("Anagramas de la palabra",word,listOfAnagrams)  
#Llamado del metodo
createListOfWords(word)

#Cabe destacar que se pudo usar una api como http://www.anagramica.com/api que nos permitiria simplemente entregarle la palabra y
#nos retornaria todos los anagramas de la palabra, de hecho seria mas eficiente ya que solo se haria un Request y no un request por permutacion
#como se hace aqui, sin embargo decidi hacerlo asi como reto personal.


#Aclaraciones:
#Solo funciona con palabras en ingles, se puede hacer en español pero seria necesario encontrar usar otra API
#Si se ingresan palabras demasiado grandes tomara demasiado tiempo obtener el resultado debido a la cantidad de request que se realizan





