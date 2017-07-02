from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'https://www.google.com'
print("now access %s"%(url))

driver.set_window_size(1024,720)
driver.get(url)

time.sleep(2)
driver.quit()