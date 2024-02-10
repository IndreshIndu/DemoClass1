from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote import switch_to


opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=opts)#"driver" is a Object. "Webdriver" is a method. "Chrome" is a class
driver.maximize_window()
driver.implicitly_wait(5)

actions=ActionChains(driver)

#Download 
r'''
driver.get("https://demo.automationtesting.in/FileDownload.html")

download_btn=driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div[1]/a')
download_btn.click()

text_box=driver.find_element(By.ID, "textbox")
text_box.send_keys("Indresh")

generate_btn=driver.find_element(By.ID, "createTxt")
actions.click(generate_btn).perform()

download_text=driver.find_element(By.ID, "link-to-download")
actions.click(download_text).perform()
'''

#Upload

r'''
driver.get("https://demo.automationtesting.in/FileUpload.html")

browse_btn=driver.find_element(By.ID, "input-4")
browse_btn.send_keys(r"C:\Users\indre\Desktop\token.txt")


#Screen shot
driver.save_screenshot(r"C:\Users\indre\Pictures\Screenshots.png")
'''



practice_site=driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[10]/a')
practice_site.click().perform()


practice_in=driver.window_handles
driver.switch_to.window(https://practice.automationtesting.in/)


#popup_close=driver.find_element(By.XPATH, '//*[@id="image-square"]/div')
#popup_close.click()

#my_wait=WebDriverWait(driver, 10)
#visible_popup_close=my_wait.until(EC.visibility_of(popup_close))
#visible_popup_close.click()
#AJAX elements (page without getting refreshed the element will appear. Like pop-ups


