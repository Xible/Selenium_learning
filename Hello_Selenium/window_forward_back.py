'''
use selenium back / forward function to change current page
'''

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

first_url = "https://www.google.com"
second_url = "https://www.google.com.tw/maps?hl=zh-TW&tab=wl"


print("now access %s" %(first_url))
driver.get(first_url)
sleep(1)

print("now access %s" %(second_url))
driver.get(second_url)
sleep(1)

print("back to %s" %(first_url))
driver.back()
sleep(1)

print("forward to %s" %(second_url))
driver.forward()
sleep(1)

print("close webdriver")
driver.quit()
