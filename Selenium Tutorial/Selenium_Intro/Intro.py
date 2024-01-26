from selenium import webdriver

# Step 1 : Launching the Chrome browser
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
#opts.add_argument("start-maximized")
driver=webdriver.Chrome(options=opts)#"driver" is a Object. "Webdriver" is a method. "Chrome" is a class
driver.maximize_window()

# Step 2 : Navigate to practice site
driver.get("https://testautomationpractice.blogspot.com/")

#Step 3 : Validation
page_title=driver.title #actual value
print(page_title)

if page_title == "Automation Testing Practice":
    print("Navigation test is pass")
else:
    print("Navigation test is failed")