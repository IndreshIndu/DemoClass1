from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Step 1 : Launching the Chrome browser
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
#opts.add_argument("start-maximized")
driver=webdriver.Chrome(options=opts)#"driver" is a Object. "Webdriver" is a method. "Chrome" is a class
driver.maximize_window()
driver.implicitly_wait(5)

# Step 2 : Navigate to practice site
driver.get("https://testautomationpractice.blogspot.com/")