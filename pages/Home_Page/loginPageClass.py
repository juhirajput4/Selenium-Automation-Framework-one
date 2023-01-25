from selenium import webdriver
from selenium.webdriver.common.by import By
class loginPageClass():
    def __init__(self, driver):
        self.driver = driver

    # Locators
    _sign_in_button = "//a[@href='/login']"
    email_field = "(//input[@id='email'])[1]"
    _pass_field = "//input[@id='password']"
    _login_button = "//input[@value='Login']"

    def getSignInField(self):
        return self.driver.find_element(By.XPATH, self._sign_in_button)

    def getEmailField(self):
        return self.driver.find_element(By.XPATH, self.email_field)

    def getPassField(self):
        return self.driver.find_element(By.XPATH, self._pass_field)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_button)

    def clickSignInButton(self):
        self.getSignInField().click()

    def enterEmailField(self, userName):
        self.getEmailField().send_keys(userName)

    def enterPassField(self, password):
        self.getPassField().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()


    def login(self, userName, password):
        self.clickSignInButton()
        self.enterEmailField(userName)
        self.enterPassField(password)
        self.clickLoginButton()
