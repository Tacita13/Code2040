#Challenge 2
import requests

TOKEN="47a85271458d345c6fb32f3c7d7c3d51"

r = requests.post('http://challenge.code2040.org/api/reverse', data = {'token':TOKEN})
print (r.content)

inputString=r.content
reversedString =inputString[::-1]

r = requests.post('http://challenge.code2040.org/api/reverse/validate', data = {'token':TOKEN, 'string':reversedString})
print(r.content)



