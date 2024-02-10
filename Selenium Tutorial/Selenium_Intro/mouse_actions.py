from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.action_chains import ActionChains



opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=opts)#"driver" is a Object. "Webdriver" is a method. "Chrome" is a class
driver.maximize_window()
driver.implicitly_wait(5)

#driver.get("https://testautomationpractice.blogspot.com/")
driver.get("https://demo.automationtesting.in/Resizable.html")
#driver.get("https://demo.guru99.com/test/simple_context_menu.html")
#driver.get("https://demo.automationtesting.in/WebTable.html")
actions=ActionChains(driver) #it is common for mouse action


#Mouse action for "Drag and Drop"
'''
source=driver.find_element(By.ID, "draggable")
target=driver.find_element(By.ID, "droppable")

actions.drag_and_drop(source, target).perform()  #",perform" is mandatory
#actions.drag_and_drop_by_offset(source, 50, 50).perform() #used for particular position
'''

#Scrolling
'''
actions.scroll_by_amount(0, 300).perform()
'''

#"Double Click"
'''
db_click=driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
#actions.scroll_to_element(db_click).perform() #scroll to element by default it will perform
actions.double_click(db_click).perform()
'''

#Right click
'''
actions.context_click(on_element)
'''

#Slider action
'''
source=driver.find_element(By.XPATH, '//*[@id="slider"]/span')
actions.drag_and_drop_by_offset(source, 200, 0).perform()
'''

#Resizable action

source=driver.find_element(By.XPATH, '//*[@id="resizable"]/div[3]')
actions.drag_and_drop_by_offset(source, 400, 500).perform()


#Right Click action
'''
right_click_btn=driver.find_element(By.XPATH, '//*[@id="authentication"]/span')
actions.context_click(right_click_btn).perform()
'''

#Mouse hovering
'''
#web_table=driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[5]/a//*[@id="header"]/nav/div/div[2]/ul/li[3]/a')
widgets=driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[5]/a')
actions.move_to_element(widgets).perform()
'''






