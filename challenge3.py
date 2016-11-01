#Challenge 3
import requests

TOKEN="47a85271458d345c6fb32f3c7d7c3d51"

r = requests.post('http://challenge.code2040.org/api/haystack', data = {'token':TOKEN})

result=r.json()
haystack=result["haystack"]
needle=result["needle"]

index=haystack.index(needle)

r = requests.post('http://challenge.code2040.org/api/haystack/validate', data = {'token':TOKEN, 'needle':index})




