from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY'in os.environ:del os.environ['HTTP_PROXY']

driver = webdriver.Chrome()
url = 'https://www.google.com'

driver.get(url)

print("tilte of current page is %s" %(driver.title))
print("url of current page is %s" %(driver.current_url))

sleep(2)
driver.quit()

