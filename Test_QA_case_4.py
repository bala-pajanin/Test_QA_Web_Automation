from selenium import webdriver
import os
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


    # To click on create account
    def create_account(self, email_address):
        
        self.driver.find_element_by_id("email_create").send_keys(email_address)

        self.driver.find_element_by_id("SubmitCreate").click()

        # wait for text <connexion settings>
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='TunnelDeCommande']/div[3]/div[1]/div[4]/h2")))

    # To fill registration form
    def registration_form(self):

        self.driver.find_element_by_id("email").send_keys("test.case.automation4@gmail.com")

        self.driver.find_element_by_id("password").send_keys("Test123/")

        self.driver.find_element_by_id("password2").send_keys("Test123/")

        self.driver.find_elements_by_class_name("lbl_checkbox")[2].click()

        self.driver.find_element_by_id("nom").send_keys("Last_test")

        self.driver.find_element_by_id("prenom").send_keys("First_test")

        self.driver.find_element_by_id("dateJour").send_keys("01")

        self.driver.find_element_by_id("dateMois").send_keys("01")

        self.driver.find_element_by_id("dateAnnee").send_keys("2000")

        self.driver.find_element_by_id("adresse").send_keys("5 Boulevard de la Madeleine")

        self.driver.find_element_by_id("codePostal").send_keys("75001")

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB)
        actions.perform()

        # Check if city populates when you enter the pin code
        ville = self.driver.find_element_by_id("ville")
        ville_state = ville.is_enabled()
        if ville_state is False:
            print("City is not populated when you enter the pin code")
            print("Registration is not successful")
        else:
            self.driver.find_element_by_id("telephonePortable").send_keys("0612345678")
            self.driver.find_element_by_id("telephoneFixe").send_keys("0123456789")
            self.driver.find_element_by_id("BtnCreationSubmit").click()



    # To close navigator
    def close_browser(self):
        self.driver.quit()



# create an Object for web_automation class
create = web_automation()

# Open chrome navigator & navigate with <https://marksandspicy.com>
create.navigate_marks_spicy()

#Click on Sign in
create.sign_in()

# To create an account
create.create_account("test.case.automation4@gmail.com")

# To fill the registration form
create.registration_form()

#To close navigator
create.close_browser()
