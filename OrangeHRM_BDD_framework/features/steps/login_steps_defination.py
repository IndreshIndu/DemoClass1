from behave import given, when, then
from selenium import webdriver 
from selenium.webdriver.common.by import By

@given(u'Chrome browser is launched')
def step_launch_browser(context):
    #def setUp(self):
    opts=webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    context.driver=webdriver.Chrome(options=opts)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
        

@when(u'User navigates to OrangeHRM Login page')
def step_navigate_to_orangehrm_login(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then(u'User should see page title as OrangeHRM')
def step_validate_navigation_to_orangehrm_login(context):
    #def test_navigation(self):
        
    expected_page_title="OrangeHRM"
    actual_page_title=context.driver.title
    assert expected_page_title == actual_page_title, "Title is not as expected"
    
    
@when(u'User enter valied ID,valied password and click Login button')
def step_enter_credentials(context):
    u_name_txt=context.driver.find_element(By.NAME, "username")
    u_name_txt.send_keys("Admin")
    
    pass_txt=context.driver.find_element(By.NAME, "password")
    pass_txt.send_keys("admin123")
    
    login_clk=context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()   



@then(u'User should navigate to Dash board menu')
def step_validation_login_url(context):
    expected_url=context.driver.current_url
    assert "dashboard/index" in expected_url, 'not in admin page'

@when(u'User enter username: "{username}", password: "{password}" and click Login button')
def step_login_with_id_pass(context,username,password):
    u_name_txt=context.driver.find_element(By.NAME, "username")
    u_name_txt.send_keys(username)
    
    pass_txt=context.driver.find_element(By.NAME, "password")
    pass_txt.send_keys(password)
    
    login_clk=context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()   

    
