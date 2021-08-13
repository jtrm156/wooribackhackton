#from urllib2 import Request, urlopen
#from urllib import urlencode, quote_plus
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
from requests import Request, Session
import json,requests,pprint,urllib
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
    "NEW_DT": "20160301",
    "INQ_STA_DT": "20210501",
    "INQ_END_DT": "20210503",
    "ACCT_KND": "J",
    "CUCD": "KRW"
  }
}

headers = {'appKey':'l7xxajP1OePkOGz3tti9noGq6kjbKesoQQL7', 'Content-Type':'application/json;charset=UTF-8'}

response = requests.post(url, data = json.dumps(values), headers = headers)
print("status code:", response.status_code)
response.raise_for_status()

results = response.json()
print(response.json())

with open("result.json", "w", encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False)

#print(json.dumps(results))
#request.get_method = lambda: 'POST'
#response_body = urlopen(request).read().decode('utf-8')
#print(response_body)
#print(type(response_body))
#jsonArray = json.loads(response_body)
#storeInfosArray = jsonArray.get("storeInfos")
#print(storeInfosArray)
#print(response_body)

#req = Request('POST', url, data=values, headers=headers)
#prepped = req.prepare()
#res = s.send(prepped)

#pprint.pprint(res.json())