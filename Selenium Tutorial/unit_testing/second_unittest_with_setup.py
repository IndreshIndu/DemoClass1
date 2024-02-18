import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class Test(unittest.TestCase):


    def setUp(self):
        opts=webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        self.driver=webdriver.Chrome(options=opts)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
    def test_navigation(self):
        
        expected_page_title="OrangeHRM"
        actual_page_title=self.driver.title
        #self.assertEqual(actual_page_title, expected_page_title, "Title is not as expected")
        assert expected_page_title == actual_page_title, "Title is not as expected"
        

    def test_login(self):
        
        u_name_txt=self.driver.find_element(By.NAME, "username")
        u_name_txt.send_keys("Admin")
        
        pass_txt=self.driver.find_element(By.NAME, "password")
        pass_txt.send_keys("admin123")
        
        login_clk=self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()   


        #expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        expected_url=self.driver.current_url
        assert "dashboard/index" in expected_url, 'not in admin page'

    #
    # def testName(self):
    #     pass


if __name__ == "__main__":
    import sys;sys.argv = ['', 'Test.login']
    unittest.main()