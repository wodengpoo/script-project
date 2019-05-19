import os
import sys
import urllib.request
import urllib
from xml.dom.minidom import *
from xml.etree import ElementTree

stList = []
stID = []
busNUM = []

def Sgetbusnm(stid):
    busNUM = []
    serviceKey = '1ZUPc%2BJmDiSiYavXUDMa1%2BbIXXZlyQjE1y%2FPZpJ88HsW28VvHpu7Sc4SS8DFMCrJlufba3pK3sf2JQtSvQ80Gg%3D%3D'
    url = 'http://ws.bus.go.kr/api/rest/stationinfo/getRouteByStation?serviceKey='

    request = urllib.request.Request(url + serviceKey + '&arsId=' + stid)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        resbody = response.read()
        # print(resbody.decode('utf-8'))
        # Dom 객체를 통한 파싱
        doc = parseString(resbody)  # 문자열 입력 파싱 함수, DOC객체 반환1
        tree = ElementTree.fromstring(str(doc.toxml()))
        elements = tree.getiterator("itemList")
        for item in elements:
            bnum = item.find("busRouteNm")
            busNUM.append(bnum.text)
        return busNUM
    return None

def Kgetbusnm(stid):
    busNUM = []
    serviceKey = '1ZUPc%2BJmDiSiYavXUDMa1%2BbIXXZlyQjE1y%2FPZpJ88HsW28VvHpu7Sc4SS8DFMCrJlufba3pK3sf2JQtSvQ80Gg%3D%3D'
    url = 'http://openapi.gbis.go.kr/ws/rest/busstationservice/route?serviceKey='

    request = urllib.request.Request(url + serviceKey + '&stationId=' + stid)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        resbody = response.read()
        # print(resbody.decode('utf-8'))
        # Dom 객체를 통한 파싱
        doc = parseString(resbody)  # 문자열 입력 파싱 함수, DOC객체 반환1
        tree = ElementTree.fromstring(str(doc.toxml()))
        elements = tree.getiterator("busRouteList")
        for item in elements:
            bnum = item.find("routeName")
            busNUM.append(bnum.text)
        return busNUM
    return None

def Sgetsttn(keyword):
    global sttnList, stID
    stList = []
    stID = []
    serviceKey = '1ZUPc%2BJmDiSiYavXUDMa1%2BbIXXZlyQjE1y%2FPZpJ88HsW28VvHpu7Sc4SS8DFMCrJlufba3pK3sf2JQtSvQ80Gg%3D%3D'
    url = 'http://ws.bus.go.kr/api/rest/stationinfo/getStationByName?serviceKey='

    request = urllib.request.Request(url + serviceKey + '&stSrch=' + keyword)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        resbody = response.read()
        # print(resbody.decode('utf-8'))
        # Dom 객체를 통한 파싱
        doc = parseString(resbody)  # 문자열 입력 파싱 함수, DOC객체 반환1
        tree = ElementTree.fromstring(str(doc.toxml()))
        elements = tree.getiterator("itemList")
        for item in elements:
            bussttn = item.find("stNm") # 정류소명
            sttnID = item.find("arsId")  # 정류소ID
            stList.append(bussttn.text)
            stID.append(sttnID.text)
        #print(stID)
        #print(stList)
        return stList, stID
    return None

def Kgetsttn(keyword):
    global stList, stID
    stList = []
    stID = []
    serviceKey = '1ZUPc%2BJmDiSiYavXUDMa1%2BbIXXZlyQjE1y%2FPZpJ88HsW28VvHpu7Sc4SS8DFMCrJlufba3pK3sf2JQtSvQ80Gg%3D%3D'
    url = 'http://openapi.gbis.go.kr/ws/rest/busstationservice?serviceKey='

    request = urllib.request.Request(url + serviceKey + '&keyword=' + keyword)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        resbody = response.read()
        # print(resbody.decode('utf-8'))
        # Dom 객체를 통한 파싱
        doc = parseString(resbody)  # 문자열 입력 파싱 함수, DOC객체 반환1
        tree = ElementTree.fromstring(str(doc.toxml()))
        elements = tree.getiterator("busStationList")
        for item in elements:
            bussttn = item.find("stationName") #정류소명
            sttnID = item.find("stationId") #정류소ID
            stList.append(bussttn.text)
            stID.append(sttnID.text)
        #print(stID)
        #print(stList)
        return stList, stID
    return None

if __name__ == "__main__":
    key = urllib.parse.quote("강남")
    Sgetsttn(key)