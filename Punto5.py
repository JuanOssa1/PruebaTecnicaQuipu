from urllib import response
from urllib.request import urlopen
import requests as rq
import json

URL="https://api.dictionaryapi.dev/api/v2/entries/en/hello"
response= rq.get(URL, timeout=2.50)
dict=response.json()

jsonString=json.dumps(dict)

#jsonData = json.loads(response.text)
jsonInList= json.loads(jsonString)
print(jsonInList[0]['word'])
