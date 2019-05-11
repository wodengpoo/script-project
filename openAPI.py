import os
import sys
import urllib.request
import xml.parsers.expat
from urllib.parse import urlparse

def start_element(name, attrs):
    print('Start element:', name, attrs)
def char_data(data):
    print('Character data:', repr(data))

serviceKey = '1ZUPc%2BJmDiSiYavXUDMa1%2BbIXXZlyQjE1y%2FPZpJ88HsW28VvHpu7Sc4SS8DFMCrJlufba3pK3sf2JQtSvQ80Gg%3D%3D'
url = 'http://openapi.tago.go.kr/openapi/service/BusSttnInfoInqireService/getCtyCodeList?output=xml&serviceKey='
request = urllib.request.Request(url + serviceKey)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if rescode == 200:
    resbody = response.read()
    #print(resbody.decode('utf-8'))
    pa = xml.parsers.expat.ParserCreate()
    pa.StartElementHandler = start_element
    pa.CharacterDataHandler = char_data
    pa.Parse(resbody)
