#from urllib2 import Request, urlopen
#from urllib import urlencode, quote_plus
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus

import json
import pandas as pd
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
    "INQ_STA_DT": "20210101",
    "INQ_END_DT": "20210310",
    "NEW_DT": "20140522",
    "ACCT_KND": "P",
    "CUCD": "KRW"
  }
}

headers = { 'appkey':'l7xxajP1OePkOGz3tti9noGq6kjbKesoQQL7',  'token':'', }
request = Request(url
, data=values
, headers=headers)
request.get_method = lambda: 'POST'
response_body = urlopen(url).read().decode('utf-8')
jsonArray = json.loads(response_body)
storeInfosArray = jsonArray.get("storeInfos")
print(storeInfosArray)
#print(response_body)
