import urllib.request as ul
import xml.dom.minidom as doms
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.syderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = 'http://know.kfri.go.kr/openapi/cyberLib/peridodicalIndexSearch.do?'
key = 'keyValue=fZGmHhe%2BTsKPdIFP0icM0MT2qhJOXiIBCUOfpWsJdN8%3D'
format = '&version=1.0&searchGbn=TITLE'

req = ul.Request(url + key + format)

response = ul.urlopen(req)
rD = doms.parse(response)
print(rD)