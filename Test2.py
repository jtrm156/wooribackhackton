"""from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.coupang.com/vp/products/323907063?itemId=1037089428&vendorItemId=5491454088&isAddedCart=​")
time.sleep(5) 
a = driver.find_element_by_xpath("//*[@id='btfTab']/ul[1]/li[2]")
a.click()
time.sleep(5) 
html = driver.page_source
soup = BeautifulSoup(html,"html.parser")
res = soup.find_all(class_="sdp-review__article__list__headline")
for n in res:
    print(n.get_text())
"""

"""
import time
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("아이온")
elem.send_keys(Keys.RETURN)
"""
