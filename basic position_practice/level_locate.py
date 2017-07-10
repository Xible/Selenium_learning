'''
下方會練習使用WebDriverWait以及ActionChains來操作層級定位
ActionChains : http://www.15jb.net/article/38622.html
WebDriverWait : http://www.cnblogs.com/saryli/p/4293670.html
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os 

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('level_locate.html')
driver.get(file_path)

driver.find_element_by_link_text('Link1').click()

#設置等待時間，使用WebDriverWait來設定等待時間。超過10秒或者until內的條件成立則結束
WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_id('dropdown1').is_displayed())
menu = driver.find_element_by_id('dropdown1').find_element_by_link_text('Another action')

#ActionChains是模擬滑鼠動作，會將操作動作依序執行。需要在後方打上perform()
webdriver.ActionChains(driver).move_to_element(menu).perform()
sleep(2)

#以下為練習
driver.find_element_by_link_text('Link2').click()
WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_id('dropdown2').is_displayed())
menu2 = driver.find_element_by_id("dropdown2").find_element_by_link_text('Action')

webdriver.ActionChains(driver).move_to_element(menu2).perform()
sleep(2)


driver.quit()