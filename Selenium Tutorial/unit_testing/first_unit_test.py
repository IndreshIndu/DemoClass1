import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestOrangeHRM(unittest.TestCase):

    def test_navigation(self):
        opts=webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver=webdriver.Chrome(options=opts)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        expected_page_title="OrangeHRM"
        actual_page_title=driver.title
        #self.assertEqual(actual_page_title, expected_page_title, "Title is not as expected")
        assert expected_page_title == actual_page_title, "Title is not as expected"
        

    def login(self):
        opts=webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver=webdriver.Chrome(options=opts)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        u_name_txt=driver.find_element(By.NAME, "username")
        u_name_txt.send_keys("Admin")
        
        pass_txt=driver.find_element(By.NAME, "password")
        
        
        
        
        
        
        
           

    
    
    
    
    
    