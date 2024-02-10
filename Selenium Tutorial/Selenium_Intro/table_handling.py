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

web_table=driver.find_element(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr[2]/td[1]")
#print(web_table.text)

web_table1=driver.find_element(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr[2]/td[2]")
#print(web_table1.text)
'''
for i in range(2,8):
    for j in range(1,5):
        cell_1=driver.find_element(By.XPATH, f"//*[@id='HTML1']/div[1]/table/tbody/tr[{i}]/td[{j}]")
        print(cell_1.text)
'''


expected_book_name=input("enter the book name")

for i in range (2,8):
    cell_1=driver.find_element(By.XPATH, f"//*[@id='HTML1']/div[1]/table/tbody/tr[{i}]/td[1]")
    cell_2=driver.find_element(By.XPATH, f"//*[@id='HTML1']/div[1]/table/tbody/tr[{i}]/td[4]")
    
    actual_book_name=cell_1.text
    if actual_book_name==expected_book_name:
        print(cell_2.text)
    
    #print(cell_1.text)
    #print(cell_2.text)    

    





    
       
    















time.sleep(20)
driver.quit()