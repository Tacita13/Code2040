#******************************************************************
#
#   Programmer : Isamar López Rodríguez 
#   Challenge 4                          Code 2040 Tech Assesment
#   File       : challenge4.py           date : 10/31/16
#
#******************************************************************
#  Description :This file contains a json request post to identify
#  the words that start with a given prefix and place the words
#  that do not start with such prefix in a newly formed array.
#
#******************************************************************
import requests
import json 

#fixed token variable
TOKEN="47a85271458d345c6fb32f3c7d7c3d51"

#gets given parameters
r = requests.post('http://challenge.code2040.org/api/prefix', data = {'token':TOKEN})

#identifyies array and result variable
result=r.json()
array=result["array"]
prefix=result["prefix"]

#new array that will contain those words without the prefix
resultArray=[]

#loop that navigates each element of the array in the search
#for words with the given prefix and only stores those without it in the resultArray
for element in array:
	if element[0:len(prefix)]!=prefix:
		resultArray.append(element)

#resulting post with token and array
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
r = requests.post('http://challenge.code2040.org/api/prefix/validate', data = json.dumps({'token':TOKEN, 'array':resultArray}), headers=headers)



