from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path="D:/Python/phantomjs-2.1.1-windows/bin/phantomjs")
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
pageSource = driver.page_source
bsObj = BeautifulSoup(pageSource)
print(bsObj.find(id = "content").get_text())

time.sleep(1)
print(driver.find_element_by_id('content').text)
driver.close()
