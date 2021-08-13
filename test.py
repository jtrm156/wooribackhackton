#from urllib2 import Request, urlopen
#from urllib import urlencode, quote_plus
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import json
import pandas as pd
from bs4 import BeautifulSoup
import urllib

url = 'https://openapi.wooribank.com:444/oai/wb/v1/finance/getAccTransList'

values  = {
  "dataHeader": {
    "UTZPE_CNCT_IPAD": "",
    "UTZPE_CNCT_MCHR_UNQ_ID": "",
    "UTZPE_CNCT_TEL_NO_TXT": "",
    "UTZPE_CNCT_MCHR_IDF_SRNO": "",
    "UTZ_MCHR_OS_DSCD": "",
    "UTZ_MCHR_OS_VER_NM": "",
    "UTZ_MCHR_MDL_NM": "",
    "UTZ_MCHR_APP_VER_NM": ""
  },
  "dataBody": {
    "INQ_ACNO": "1002123456789",
    "NEW_DT": "20160301",
    "INQ_STA_DT": "20190101",
    "INQ_END_DT": "20190613",
    "ACCT_KND": "J",
    "CUCD": "KRW"
  }
}
headers = {'appKey':'l7xxajP1OePkOGz3tti9noGq6kjbKesoQQL7', 'Content-Type' : 'application/json;charset=UTF-8'}

request = Request(url
, data=values
, headers=headers)
request.get_method = lambda: 'POST'
print(type(request))
response_body = urlopen(request).read()
print(results)

#encData = urlencode(values)
#postData = bytes(encData,encoding='utf-8')
#req = Request(url,data=postData,headers=headers)
#f = urlopen(req)
#print(f.info())
#print(f.read().decode('utf-8'))

#res = urllib.request.urlopen(url)
#print(res.status)

