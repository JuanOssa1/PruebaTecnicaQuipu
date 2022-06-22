from itertools import permutations
import requests as rq
import json

word=input()
#print([''.join(p) for p in permutations(word)])

def searchWordInDictionary(word):
    URL="https://api.dictionaryapi.dev/api/v2/entries/en/"+word
    response= rq.get(URL, timeout=2.50)

    if(response.status_code==200):
        dict=response.json()
        jsonString=json.dumps(dict)
        jsonInList= json.loads(jsonString)
        return jsonInList[0]['word']   
    else:
        print("Esa palabra no existe")
        

def createListOfWords(word):
    listOfPermutations=permutations(word)
    for i in list(listOfPermutations):
        wordToValidate="".join(i)
        searchWordInDictionary(wordToValidate)

createListOfWords(word)




