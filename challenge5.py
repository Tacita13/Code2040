#******************************************************************
#
#   Programmer : Isamar López Rodríguez 
#   Challenge 5                          Code 2040 Tech Assesment
#   Archivo    : challenge5.py           date : 10/31/16
#
#******************************************************************
#  Description :This file contains a json request post to make a
#  date format out of the given intervals and datestamp
#
#******************************************************************
import requests
import json 
import datetime
import time

#fixed token variable
TOKEN="47a85271458d345c6fb32f3c7d7c3d51"

#gets given parameters
r = requests.post('http://challenge.code2040.org/api/dating', data = {'token':TOKEN})

result=r.json()
# initilizes viables with given parameters
dateString=result['datestamp']
interval=result['interval']

#cleans the date format to make it easier to work with
dateString=dateString.replace("T", " ").replace("Z","")
#initilizes a datetime for the date given and converts it to unixtime
unixtime=time.mktime(datetime.datetime.strptime(dateString,"%Y-%m-%d %H:%M:%S").timetuple())
#sums the interval to the unixtime
unixtime=unixtime+int(interval)
#convert unixtime back to date ISO format
outputdate=datetime.datetime.fromtimestamp(unixtime).isoformat()
#append "Z" because ISO format fails to put it
outputdate=outputdate+"Z"

#resulting post with token and datemap
r = requests.post('http://challenge.code2040.org/api/dating/validate', data = {'token':TOKEN, 'datestamp':outputdate})

