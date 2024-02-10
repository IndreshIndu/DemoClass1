from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
#opts.add_argument("start-maximized")
driver=webdriver.Chrome(options=opts)#"driver" is a Object. "Webdriver" is a method. "Chrome" is a class
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com/")

driver.switch_to.frame("frame-one796456169")

job_drop=driver.find_element(By.ID, "RESULT_RadioButton-3")
drop_down_selector=Select(job_drop)
#drop_down_selector.select_by_index(2)
#drop_down_selector.select_by_value("Radio-2")
drop_down_selector.select_by_visible_text("Manager")