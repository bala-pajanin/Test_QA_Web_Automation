from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class web_automation():

    # To do navigation
    def navigate_marks_spicy(self):
        driverLocation = "C:\\pycharm_python\\libs\\chromedriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        self.driver = webdriver.Chrome(driverLocation)

        self.driver.maximize_window()
        self.driver.get("https://marksandspicy.com")

        # To validate home page
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "login")))

    # To click on Sign In
    def sign_in(self):

        # To click on Sign in
        self.driver.find_element_by_class_name("login").click()

        # wait for sign in button
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "SubmitLogin")))

    # To do login with username & password and check if there is an error displayed
    def check_login(self, username, password):
        self.driver.find_element_by_xpath("//*[@id='email']").send_keys(username)

        self.driver.find_element_by_xpath("//*[@id='passwd']").send_keys(password)

        self.driver.find_element_by_id("SubmitLogin").click()

        self.driver.implicitly_wait(3)

        # Check if there is an error displayed
        check_username = self.driver.find_element_by_xpath("//*[@id='login_form']/div/div[1]").get_attribute("class")

        check_password = self.driver.find_element_by_xpath("//*[@id='login_form']/div/div[2]").get_attribute("class")

        if check_username == "form-group" and check_password == "form-group":
            print("both username and/or password are not correct")

    # To close navigator
    def close_browser(self):
        self.driver.quit()



# create an Object for web_automation class
login = web_automation()

# Open chrome navigator & navigate with <https://marksandspicy.com>
login.navigate_marks_spicy()

#Click on Sign in
login.sign_in()

# To do login with username & password and check if there is an error displayed
login.check_login("test@test.com", "ThisIs@T3st")

#To close navigator
login.close_browser()
