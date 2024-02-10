from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import stat
from pip._vendor.rich import status


opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=opts)#"driver" is a Object. "Webdriver" is a method. "Chrome" is a class
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com/")



name=input("Enter the product")
pages=driver.find_element(By.XPATH, "//*[@id='pagination']/li")
page_count=len(pages)
status=True

for k in range (1,page_count+1):
    p2=driver.find_element(By.XPATH, f"//*[@id='pagination']/li[{k}]/a").click()
    
    rows=driver.find_element(By.XPATH, '//*[@id="productTable"]/tbody/tr')
    rows_count=len(rows)
    for j in range (1,rows_count+1):
        c1=driver.find_element(By.XPATH, f"//*[@id='productTable']/tbody/tr[{j}]/td[2]")
        c2=driver.find_element(By.XPATH, f"//*[@id='productTable']/tbody/tr[{j}]/td[3]")
                    
        actual_product_name=c1.text
        if actual_product_name==name:
            print(c2.text) 
            status=False
            
    if status==False:
        break     

    
        
            
