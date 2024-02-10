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

'''
name_txtbox=driver.find_element(By.ID, "name")
name_txtbox.send_keys("Indresh")


name_txtbox=driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
name_txtbox.send_keys("Selenium")

search_box=driver.find_element(By.CLASS_NAME, "wikipedia-search-button")
search_box.click()

#time.sleep(2)
#before=driver.current_window_handle
#print(before)

'''
'''
search_option=driver.find_element(By.XPATH, "//*[@id='wikipedia-search-result-link']/a")
search_option.click()

tottal_windows=driver.window_handles
driver.switch_to.window(tottal_windows[1])

#after=driver.current_window_handle
#print(after)

talk_option=driver.find_element(By.XPATH, "//*[@id='ca-talk']/a/span")
talk_option.click()

tottal_windows=driver.window_handles
driver.switch_to.window(tottal_windows[0])
'''
'''
alert_btn=driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button[1]")
alert_btn.click()

driver.switch_to.alert.accept()


confirm_box=driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button[2]")
confirm_box.click()

driver.switch_to.alert.dismiss()


prompt_box=driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button[3]")
prompt_box.click()

driver.switch_to.alert.send_keys("Indresh")
driver.switch_to.alert.accept()
'''


driver.switch_to.frame("frame-one796456169")

frames_name=driver.find_element(By.ID, "RESULT_TextField-0")
frames_name.send_keys("Indresh")

frames_dob=driver.find_element(By.ID, "RESULT_TextField-2")
frames_dob.send_keys("17/02/2000")

frames_mf=driver.find_element(By.XPATH, "//*[@id='q2']/table/tbody/tr[1]/td/label")
frames_mf.click()

frames_job=driver.find_element(By.ID, "RESULT_RadioButton-3")
frames_job.click()

frames_qa=driver.find_element(By.XPATH, "//*[@id='RESULT_RadioButton-3']")
frames_qa.click()


frames_subm=driver.find_element(By.ID, "FSsubmit")
frames_subm.click()

