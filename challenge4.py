#Challenge 4

import requests
import json 

TOKEN="47a85271458d345c6fb32f3c7d7c3d51"

r = requests.post('http://challenge.code2040.org/api/prefix', data = {'token':TOKEN})

result=r.json()
array=result["array"]
prefix=result["prefix"]
resultArray=[]
print(array)
print(prefix)
for element in array:
	if element[0:len(prefix)]!=prefix:
		resultArray.append(element)


print (resultArray)
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
r = requests.post('http://challenge.code2040.org/api/prefix/validate', data = json.dumps({'token':TOKEN, 'array':resultArray}), headers=headers)
print(r.content)


