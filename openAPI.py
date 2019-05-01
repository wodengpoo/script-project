import urllib.request as ul
import xml.dom.minidom as doms
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.syderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = 'http://data.ex.co.kr/exopenapi/restinfo/restConvList'
key = '?ServiceKey=1ZUPc%2BJmDiSiYavXUDMa1%2BbIXXZlyQjE1y%2FPZpJ88HsW28VvHpu7Sc4SS8DFMCrJlufba3pK3sf2JQtSvQ80Gg%3D%3D'
format = '&type=xml'

req = ul.Request(url + key + format)

response = ul.urlopen(req)
rD = doms.parse(response)
print(rD)