import os
import sys
import urllib.request
from xml.dom.minidom import *
#한 화면만 고집하지말고, 막대그래프도 넣고, 여러 그림 넣어도 되고, 5분 전에 소리나기 .
cityCodeToStr = dict()
cityStrToCode = dict()

def getData():
    global cityCodeToStr, cityStrToCode
    serviceKey = '1ZUPc%2BJmDiSiYavXUDMa1%2BbIXXZlyQjE1y%2FPZpJ88HsW28VvHpu7Sc4SS8DFMCrJlufba3pK3sf2JQtSvQ80Gg%3D%3D'
    url = 'http://openapi.tago.go.kr/openapi/service/BusSttnInfoInqireService/getCtyCodeList?output=xml&serviceKey='
    request = urllib.request.Request(url + serviceKey)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        resbody = response.read()
        # print(resbody.decode('utf-8'))
        # Dom 객체를 통한 파싱
        doc = parseString(resbody)  # 문자열 입력 파싱 함수, DOC객체 반환1
        # print(doc.toxml())
        res = doc.childNodes  # 맨 처음 자식노드들, response
        body = res[0].childNodes  # 도시 번호가 들어있는 노드 header 와 body
        items = body[1].childNodes  # body에 도시 정보가 들어있으므로, 그걸 사용한다. items
        for i in items[0].childNodes:
            factor = i.childNodes
            # print(factor[0].firstChild, factor[1].firstChild)
            cityCodeToStr[factor[0].firstChild.data] = factor[1].firstChild.data
            cityStrToCode[factor[1].firstChild.data] = factor[0].firstChild.data
        # print(cityCodeToStr)

if __name__ == "__main__":
    getData()