from itertools import permutations
import requests as rq
import json

word=input()

def searchWordInDictionary(word):
    URL="https://api.dictionaryapi.dev/api/v2/entries/en/"+word
    response= rq.get(URL, timeout=2.50)

    if(response.status_code==200):
        dict=response.json()
        jsonString=json.dumps(dict)
        jsonInList= json.loads(jsonString)
        return jsonInList[0]['word']   
    else:
        return ""
        
def createListOfWords(word):
    listOfAnagrams=[]
    listOfPermutations=permutations(word)
    for i in list(listOfPermutations):
        wordToValidate="".join(i)
        if(len(searchWordInDictionary(wordToValidate))>=1):
            listOfAnagrams.append(searchWordInDictionary(wordToValidate))
    if(len(listOfAnagrams)==2):
        print("This word only have his own combination")
    else:
        print(listOfAnagrams)  

createListOfWords(word)




