#Challenge 5

import requests
import json 
import datetime
import time

TOKEN="47a85271458d345c6fb32f3c7d7c3d51"

r = requests.post('http://challenge.code2040.org/api/dating', data = {'token':TOKEN})

result=r.json()

dateString=result['datestamp']
interval=result['interval']

dateString=dateString.replace("T", " ").replace("Z","")
unixtime=time.mktime(datetime.datetime.strptime(dateString,"%Y-%m-%d %H:%M:%S").timetuple())
unixtime=unixtime+int(interval)
outputdate=datetime.datetime.fromtimestamp(unixtime).isoformat()
outputdate=outputdate+"Z"

r = requests.post('http://challenge.code2040.org/api/dating/validate', data = {'token':TOKEN, 'datestamp':outputdate})

