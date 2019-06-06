import os
import sys
import urllib.request
import urllib
from xml.dom.minidom import *
from xml.etree import ElementTree

stList = [] #버스 정류장 이름
stID = [] #정류장 고유 번호
busNUM = [] # 버스 번호
busRT = [] # 버스 ID

#버스 번호 알아내는 함수
def Sgetbusnm(stid):
    busNUM = []
    busRT = []
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
            brt = item.find("busRouteId")
            busNUM.append(bnum.text)
            busRT.append(brt.text)
        return busNUM, busRT
    return None

def Kgetbusnm(stid):
    busNUM, busRT = [], []
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
    for i in range(len(busNUM)):
        serviceKey = '1ZUPc%2BJmDiSiYavXUDMa1%2BbIXXZlyQjE1y%2FPZpJ88HsW28VvHpu7Sc4SS8DFMCrJlufba3pK3sf2JQtSvQ80Gg%3D%3D'
        url = 'http://openapi.gbis.go.kr/ws/rest/busrouteservice?serviceKey='

        request = urllib.request.Request(url + serviceKey + '&keyword=' + busNUM[i])
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
                found = item.find("routeName")
                if busNUM[i] != found.text: continue
                brt = item.find("routeId")
                busRT.append(brt.text)
                break
    #print(busNUM, busRT)
    return busNUM, busRT

#정류장 이름 알아내는 함수
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
        print(stID)
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

#정류장 고유 번호로, 버스정보 알아내는 함수
#알아내야할 목록 : 배차간격, 버스 첫차/막차(정류소 고유 번호, 노선id), 버스 도착까지 남은시간(정류소 고유번호), 다음역

def SgetbusInfo(stid, busid, busnm):
    gapbustime = ''
    busarrivetime = ''
    nextsttn = ''
    F_TM = ''
    L_TM = ''
    serviceKey = '1ZUPc%2BJmDiSiYavXUDMa1%2BbIXXZlyQjE1y%2FPZpJ88HsW28VvHpu7Sc4SS8DFMCrJlufba3pK3sf2JQtSvQ80Gg%3D%3D'
    url = 'http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey='

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
            found = item.find("rtNm")
            if busnm != found.text: continue
            arr1time = item.find("arrmsg1")  # 첫번째 버스 도착시간
            term = item.find("term")  # 배차간격
            nxtStn = item.find("nxtStn")    # 다음역
            busarrivetime = arr1time.text
            gapbustime = term.text
            nextsttn = nxtStn.text
            break


    serviceKey = '1ZUPc%2BJmDiSiYavXUDMa1%2BbIXXZlyQjE1y%2FPZpJ88HsW28VvHpu7Sc4SS8DFMCrJlufba3pK3sf2JQtSvQ80Gg%3D%3D'
    url = 'http://ws.bus.go.kr/api/rest/stationinfo/getBustimeByStation?serviceKey='

    request = urllib.request.Request(url + serviceKey + '&arsId=' + stid + '&busRouteId=' + busid)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        resbody = response.read()
        print(resbody.decode('utf-8'))
        # Dom 객체를 통한 파싱
        doc = parseString(resbody)  # 문자열 입력 파싱 함수, DOC객체 반환1
        tree = ElementTree.fromstring(str(doc.toxml()))
        elements = tree.getiterator("itemList")
        for item in elements:
            found = item.find("busRouteId")
            if busid != found.text: continue
            arr1time = item.find("firstBusTm")  # 첫차
            arr2time = item.find("lastBusTm")  # 막차
            F_TM = arr1time.text
            L_TM = arr2time.text
            break
    return gapbustime, busarrivetime, nextsttn, F_TM, L_TM


def KgetbusInfo(stid, busid, busnm):
    gapbustime = ''
    gapLT = ''
    busarrivetime = ''
    nextsttn = ''
    F_TM = ''
    F2_TM = ''
    L_TM = ''
    offset = ''
    serviceKey = '1ZUPc%2BJmDiSiYavXUDMa1%2BbIXXZlyQjE1y%2FPZpJ88HsW28VvHpu7Sc4SS8DFMCrJlufba3pK3sf2JQtSvQ80Gg%3D%3D'
    url = 'http://openapi.gbis.go.kr/ws/rest/busrouteservice/info?serviceKey='

    request = urllib.request.Request(url + serviceKey + '&routeId=' + busid)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        resbody = response.read()
        # print(resbody.decode('utf-8'))
        # Dom 객체를 통한 파싱
        doc = parseString(resbody)  # 문자열 입력 파싱 함수, DOC객체 반환1
        tree = ElementTree.fromstring(str(doc.toxml()))
        elements = tree.getiterator("busRouteInfoItem")
        for item in elements:
            found = item.find("routeId")
            if busid != found.text: continue
            term = item.find("peekAlloc")  # 배차간격
            ftm, ltm = item.find("upFirstTime"), item.find("upLastTime")
            ftm2 = item.find("downFirstTime")
            gapbustime = term.text
            F_TM = ftm.text
            F2_TM = ftm2.text
            L_TM = ltm.text
            break
    serviceKey = '1ZUPc%2BJmDiSiYavXUDMa1%2BbIXXZlyQjE1y%2FPZpJ88HsW28VvHpu7Sc4SS8DFMCrJlufba3pK3sf2JQtSvQ80Gg%3D%3D'
    url = 'http://openapi.gbis.go.kr/ws/rest/busrouteservice/station?serviceKey='

    request = urllib.request.Request(url + serviceKey + '&routeId=' + busid)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        resbody = response.read()
        # print(resbody.decode('utf-8'))
        # Dom 객체를 통한 파싱
        doc = parseString(resbody)  # 문자열 입력 파싱 함수, DOC객체 반환1
        tree = ElementTree.fromstring(str(doc.toxml()))
        elements = tree.getiterator("busRouteStationList")
        on = False
        for item in elements:
            found = item.find("stationId")
            #print(found.text)
            if on == False and stid != found.text: continue
            elif on == False:
                on = True
                continue
            if on:
                nstn = item.find("stationName")
                stationSeq = item.find("stationSeq")
                nextsttn = nstn.text
                #print(nextsttn)
                offset = stationSeq.text
                break

    serviceKey = '1ZUPc%2BJmDiSiYavXUDMa1%2BbIXXZlyQjE1y%2FPZpJ88HsW28VvHpu7Sc4SS8DFMCrJlufba3pK3sf2JQtSvQ80Gg%3D%3D'
    url = 'http://openapi.gbis.go.kr/ws/rest/busarrivalservice/station?serviceKey='

    request = urllib.request.Request(url + serviceKey + '&stationId=' + stid)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        resbody = response.read()
        print(resbody.decode('utf-8'))
        # Dom 객체를 통한 파싱
        doc = parseString(resbody)  # 문자열 입력 파싱 함수, DOC객체 반환1
        tree = ElementTree.fromstring(str(doc.toxml()))
        elements = tree.getiterator("busRouteInfoItem")
        on = False
        for item in elements:
            found = item.find("stationId")
            if stid != found.text: continue
            else:
                on = True
                continue
            if on:
                nstn = item.find("stationName")
                nxtStn = nstn.text
                nextsttn = nxtStn
                break

    serviceKey = '1ZUPc%2BJmDiSiYavXUDMa1%2BbIXXZlyQjE1y%2FPZpJ88HsW28VvHpu7Sc4SS8DFMCrJlufba3pK3sf2JQtSvQ80Gg%3D%3D'
    url = 'http://openapi.gbis.go.kr/ws/rest/busarrivalseㄹvice/station?serviceKey='

    request = urllib.request.Request(url + serviceKey + '&stationId=' + stid)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        resbody = response.read()
        # print(resbody.decode('utf-8'))
        # Dom 객체를 통한 파싱
        doc = parseString(resbody)  # 문자열 입력 파싱 함수, DOC객체 반환1
        tree = ElementTree.fromstring(str(doc.toxml()))
        elements = tree.getiterator("busArrivalList")
        for item in elements:
            found = item.find("routeId")
            if busid != found.text: continue
            arr = item.find("predictTime1")
            busarrivetime = arr.text
        if busarrivetime == '':
            busarrivetime = '-'
        else:
            busarrivetime += '분'

    return gapbustime, busarrivetime, nextsttn, F_TM, L_TM, F2_TM, gapLT, offset


if __name__ == "__main__":
    key = urllib.parse.quote("강남")
    Sgetsttn(key)