#from urllib2 import Request, urlopen
#from urllib import urlencode, quote_plus
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
from requests import Request
import json,requests,urllib
import pandas as pd

url = 'https://testapi.openbanking.or.kr/v2.0/account/transaction_list/fin_num'

params = {
'bank_tran_id' : 'M202112175U000000111',
'fintech_use_num' : '120211217588932285306315',
'inquiry_type' : 'A',
'inquiry_base' : 'D',
'from_date' : '20210501',
'from_time' : '100000',
'to_date' : '20210503',
'to_time' : '110000',
'sort_order' : 'D',
'tran_dtime' : '20210502070430'
}

headers = {'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiIxMTAwNzcyNDExIiwic2NvcGUiOlsiaW5xdWlyeSIsImxvZ2luIiwidHJhbnNmZXIiXSwiaXNzIjoiaHR0cHM6Ly93d3cub3BlbmJhbmtpbmcub3Iua3IiLCJleHAiOjE2Mjc2NTI2MzcsImp0aSI6IjgxNGQ3ZGFhLWQwN2QtNDYzNC1iMDAyLWRiMGEzY2JlNjZlNSJ9.BKpwW0CJr1aPLPs1nAZzkOajSTTsLA83_fjNGXVln8M'}

response = requests.get(url, params = params, headers = headers)
print("status code:", response.status_code)
response.raise_for_status()

results = response.json()

#print(json.dumps(results))

print(response.json())

with open("result2.json", "w", encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False)