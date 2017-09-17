from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('button_group.html')

driver.get(file_path)
sleep(1)

#定位text是second的按鈕

buttons = driver.find_element_by_class_name('btn-group').find_elements_by_class_name('btn')
for btn in buttons:
    if btn.text == 'second': 
        print ('find second button')

sleep(1)
driver.quit()