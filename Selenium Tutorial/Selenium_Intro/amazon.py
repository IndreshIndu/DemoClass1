from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select




# Step 1 : Launching the Chrome browser
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
#opts.add_argument("start-maximized")
driver=webdriver.Chrome(options=opts)#"driver" is a Object. "Webdriver" is a method. "Chrome" is a class
driver.maximize_window()
driver.implicitly_wait(5)

# Step 2 : Navigate to practice site
driver.get("https://testautomationpractice.blogspot.com/")
#driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=155259815513&hvpone=&hvptwo=&hvadid=674842289437&hvpos=&hvnetw=g&hvrand=10895727330363413307&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007768&hvtargid=kwd-10573980&hydadcr=14453_2316415&gad_source=1")


search_bar=driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']")
search_bar.click()
search_bar.send_keys("mobile")

select_opt=driver.find_element(By.XPATH, "//*[@id='nav-flyout-searchAjax']/div[2]/div/div[1]/div[6]/div/div")
select_opt.click()


'''
driver.switch_to.frame("frame-one796456169")

job_drop=driver.find_element(By.ID, "RESULT_RadioButton-3")
drop_down_selector=Select(job_drop)
#drop_down_selector.select_by_index(2)
#drop_down_selector.select_by_value("Radio-2")
drop_down_selector.select_by_visible_text("Manager")

'''
