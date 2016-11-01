#******************************************************************
#
#   Programmer : Isamar López Rodríguez 
#   Challenge 3                          Code 2040 Tech Assesment
#   File       : challenge3.py           date : 10/31/16
#
#******************************************************************
#  Description :This file contains a json request post to find the
#  string needle in the array haystack
#
#******************************************************************
import requests

#fixed token variable
TOKEN="47a85271458d345c6fb32f3c7d7c3d51"

#gets given parameters
r = requests.post('http://challenge.code2040.org/api/haystack', data = {'token':TOKEN})

#initilizes variables to find needle
result=r.json()
haystack=result["haystack"]
needle=result["needle"]

#index functions gets the position where needle is located
index=haystack.index(needle)

#resulting post with token and needle
r = requests.post('http://challenge.code2040.org/api/haystack/validate', data = {'token':TOKEN, 'needle':index})




