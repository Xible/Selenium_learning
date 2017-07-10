from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
file_path =  'file:///' + os.path.abspath('operate_element.html')
driver.get(file_path)

# click
driver.find_element_by_link_text('Link1').click()
sleep(1)
driver.find_element_by_link_text('Link1').click()

# send_keys
element = driver.find_element_by_name('q')
element.send_keys('something')
sleep(1)

# clear
element.clear()
sleep(1)

driver.quit()