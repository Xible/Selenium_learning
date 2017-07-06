'''
由於html中有引用jquery，所以可以使用jquery的$()及fadeOut()等方法 
'''

from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('form.html')
print(file_path)

driver.get(file_path)

#by id
driver.find_element_by_id('inputEmail').click()

#by name
driver.find_element_by_name('password').click()

#by tagname
print(driver.find_element_by_tag_name('form').get_attribute('class'))

#by class_name
e = driver.find_element_by_class_name('controls')
driver.execute_script('$(arguments[0]).fadeOut().fadeIn()',e)
sleep(1)

#by link text
link = driver.find_element_by_link_text('register')
driver.execute_script('$(arguments[0]).fadeOut().fadeIn()',link)
sleep(1)

#by patial link text
link = driver.find_element_by_partial_link_text('reg')
driver.execute_script('$(arguments[0]).fadeOut().fadeIn()',link)
sleep(1)

#by css selector
div = driver.find_element_by_css_selector('.controls')
driver.execute_script('$(arguments[0]).fadeOut().fadeIn()',div)
sleep(1)

#by xpath
driver.find_element_by_xpath('/html/body/form/div[3]/div/label/input').click()


sleep(2)
driver.quit()