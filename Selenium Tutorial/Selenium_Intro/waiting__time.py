from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium


opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=opts)#"driver" is a Object. "Webdriver" is a method. "Chrome" is a class
driver.maximize_window()
driver.implicitly_wait(5)

actions=ActionChains(driver)

driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

'''
wait_5sec=driver.find_element(By.XPATH, '//*[@id="alert"]').click()

#time.sleep(6)
#driver.switch_to.alert.accept()

my_wait=WebDriverWait(driver,10)
alert_present=my_wait.until(EC.alert_is_present())
alert_present.accept()
'''

change_to_text=driver.find_element(By.ID, "populate-text").click()

my_time=WebDriverWait(driver,15)
selenium_lbl=my_time.until(EC.visibility_of_element_located((By.XPATH, '//h2[text()="Selenium Webdriver"]')))
print(selenium_lbl.text)











