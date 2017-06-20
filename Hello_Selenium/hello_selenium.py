# coding=utf-8
'''
Selenium 3 版本需要下載第3方webdriver 'geckodriver'，並放到firefox資料夾中
之後再將該路徑添加到環境變數path中
參考網址:https://www.zhihu.com/question/49568096
'''
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.google.com")

driver.find_element_by_id("gs_htif0").send_keys("Selenium2")
driver.find_element_by_xpath(".//*[@id='tsf']/div[2]/div[3]/center/input[1]").click()

driver.quit()