import os
import sys
import urllib.request
serviceKey = '1ZUPc%2BJmDiSiYavXUDMa1%2BbIXXZlyQjE1y%2FPZpJ88HsW28VvHpu7Sc4SS8DFMCrJlufba3pK3sf2JQtSvQ80Gg%3D%3D'
url = 'http://openapi.tago.go.kr/openapi/service/BusSttnInfoInqireService/getCtyCodeList?serviceKey='
request = urllib.request.Request(url + serviceKey)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if rescode == 200:
    resbody = response.read()
    print(resbody.decode('utf-8'))
