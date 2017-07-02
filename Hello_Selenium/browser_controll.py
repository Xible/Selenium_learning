from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(2)
print("maximize browser")

driver.maximize_window()

time.sleep(2)
print("close browser")

driver.quit()