from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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


    # To do login with username "test" & check if validation tooltip appears
    def check_login(self, username):
        self.driver.find_element_by_xpath("//*[@id='email']").send_keys(username)

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB)
        actions.perform()

        # Check if validation tooltip appears
        validtion = self.driver.find_element_by_xpath("//*[@id='login_form']/div/div[1]").get_attribute("class")
        if validtion == "form-group form-error":
            print("Validation tooltip appears")

    # To close navigator
    def close_browser(self):
        self.driver.quit()



# create an Object for web_automation class
login = web_automation()

# Open chrome navigator & navigate with <https://marksandspicy.com>
login.navigate_marks_spicy()

#Click on Sign in
login.sign_in()

# To do login with username "test" & check if validation tooltip appears
login.check_login("test")

#To close navigator
login.close_browser()
