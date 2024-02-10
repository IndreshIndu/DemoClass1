from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#1 case

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

user_name=driver.find_element(By.NAME, "username")
user_name.send_keys("Admin")

password_txt=driver.find_element(By.NAME, "password")
password_txt.send_keys("admin123")

login_btn=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

#2 case
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(5)



driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

user_name=driver.find_element(By.NAME, "username")
user_name.send_keys("admin")

password_txt=driver.find_element(By.NAME, "password")
password_txt.send_keys("admin123")

login_btn=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()



#3

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

user_name=driver.find_element(By.NAME, "username")
user_name.send_keys("admin")

password_txt=driver.find_element(By.NAME, "password")
password_txt.send_keys("Admin123")

login_btn=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()


#4

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

user_name=driver.find_element(By.NAME, "username")
user_name.send_keys("admin")

password_txt=driver.find_element(By.NAME, "password")
password_txt.send_keys("")

login_btn=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()


#5

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

user_name=driver.find_element(By.NAME, "username")
user_name.send_keys("")

password_txt=driver.find_element(By.NAME, "password")
password_txt.send_keys("Admin123")

login_btn=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()


#6 giving space b|w pass
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

user_name=driver.find_element(By.NAME, "username")
user_name.send_keys("admin")

password_txt=driver.find_element(By.NAME, "password")
password_txt.send_keys("Admin 123")

login_btn=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()






