import os
import sys
import urllib.request
from xml.dom.minidom import *

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
    #Dom 객체를 통한 파싱
    doc = parseString(resbody)  # 문자열 입력 파싱 함수, DOC객체 반환
    print(doc.toxml())
