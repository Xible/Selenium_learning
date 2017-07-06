from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)


#選擇所有的checkbox，並全部打勾
checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
sleep(1)
driver.refresh()
sleep(2)

#print 當前頁面上有多少個checkbox
print('current page has %s checkboxes' %(len(driver.find_elements_by_css_selector('input[type=checkbox]'))))

#選擇頁面上所有input，然後從中過濾出所有的checkbox並且勾選
inputs = driver.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()

sleep(1)

#把頁面上第2個checkbox的勾給拿掉

#使用pop 方法來將List中的元素移除並回傳，如不使用則不能使用點擊。
#原因是因為driver.find_elements_by_css_selector所獲取的值為list
print(type(driver.find_elements_by_css_selector('input[id=c2]')))
#driver.find_elements_by_css_selector('input[id=c2]').pop().click()

unchecks = driver.find_elements_by_css_selector('input[id=c2]')
for uncheck in unchecks:
    uncheck.click()

sleep(1)
driver.quit()