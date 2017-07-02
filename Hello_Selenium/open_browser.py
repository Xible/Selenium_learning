from selenium import webdriver
import time


driver = webdriver.Chrome()
time.sleep(3)
print("Browser will be closed")

driver.quit()
print("Browser is closed")

