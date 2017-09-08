from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os 

if 'HTTP_PROXY' in os.environ: del os.environ['HTTP_PROXY']

driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('send_keys.html')

driver.get(file_path)

# copy content of A
driver.find_element_by_id('A').send_keys((Keys.CONTROL, 'a'))
driver.find_element_by_id("A").send_keys((Keys.CONTROL, 'x'))
sleep(1)

# paste to B
driver.find_element_by_id('B').send_keys((Keys.CONTROL, 'v'))
sleep(1)

# send keys to A
driver.find_element_by_id("A").send_keys('selenium', '-', 'webdriver', Keys.SPACE, 'is', Keys.SPACE, 'better')
sleep(2)


driver.quit()