'''
Created on 2016年3月22日

@author: lyt
'''
import urllib.request 
import random
import json
from pip._vendor.requests.exceptions import HTTPError

html=json.loads('{"adf":"da","ahkghka":"adf"}')
print(html)

def getGoogle():
    response=urllib.request.urlopen("http://www.google.cn",timeout=5 )
    html=response.read()
    html=html.decode("utf-8");
    print("getGoogle")
    print(html)
def getGoogleByProxy():
    proxyList=["58.64.212.204"]
    proxy_support=urllib.request.ProxyHandler({"http":random.choice(proxyList)})
    opener=urllib.request.build_opener(proxy_support)
#     urllib.request.install_opener(opener)
#     response=urllib.request.urlopen("http://www.google.com" )
    
    response=opener.open("http://www.google.cn" )
    html=response.read()
    html=html.decode("utf-8");
    print(html)
# try:
#     getGoogleByProxy()
# except HTTPError as e:
#     print(e)
try:
    getGoogle()
except HTTPError as e:
    print(e)

if __name__!="__main__":
    data={}
    data["q"]='org.eclipse.swt'
    response=urllib.request.urlopen("http://localhost:8080/bpm/direct",data)
    html=response.read()
    html=html.decode("utf-8");
    print(html)
    