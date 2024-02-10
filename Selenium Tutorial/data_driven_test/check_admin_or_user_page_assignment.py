from selenium import webdriver
from selenium.webdriver.common.by import By
import time

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(5)


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

admin_txt=driver.find_element(By.NAME, "username")
admin_txt.send_keys("Admin")

pass_txt=driver.find_element(By.NAME, "password")
pass_txt.send_keys("admin123")

login_btn=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
login_btn.click()

def admin_page():
    try:
        admin_menu = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
        
        pim_menu = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        return admin_menu.is_displayed() and pim_menu.is_displayed()
    except:
        return False

if admin_page():
    print("Currently on admin page")
else:
    print("Currently on user page")

