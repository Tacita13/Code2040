
#******************************************************************
#
#   Programmer : Isamar López Rodríguez 
#   Challenge 2                          Code 2040 Tech Assesment
#   File       : challenge2.py           date : 10/31/16
#
#******************************************************************
#  Description :This file contains a json request post to reverse
#  a string
#
#******************************************************************
import requests

#fixed token variable
TOKEN="47a85271458d345c6fb32f3c7d7c3d51"

#gets given parameters
r = requests.post('http://challenge.code2040.org/api/reverse', data = {'token':TOKEN})
print (r.content)

#reverses the string by not writing the [begin:end: -1] and specifying the step as -1
inputString=r.content
reversedString =inputString[::-1]

#resulting post with token and string
r = requests.post('http://challenge.code2040.org/api/reverse/validate', data = {'token':TOKEN, 'string':reversedString})
print(r.content)



