from selenium import webdriver
from selenium.webdriver.common.by import By
from base.basePage import basePage

from utilities import customLogger_twoFrameworkOne as cl
import logging
import time

class loginPageClass(basePage):
    log = cl.CustomLogger(loggerName="classLogger", logLevel=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _sign_in_button = "//a[@href='/login']"
    email_field = "(//input[@id='email'])[1]"
    _pass_field = "//input[@id='password']"
    _login_button = "//button[@id='login']"

    def getSignInField(self):
        # return self.driver.find_element(By.XPATH, self._sign_in_button)
        return self.getElement(self._sign_in_button, "xpath")

    def getEmailField(self):
        # return self.driver.find_element(By.XPATH, self.email_field)
        return self.getElement(self.email_field, "xpath")

    def getPassField(self):
        # return self.driver.find_element(By.XPATH, self._pass_field)
        return self.getElement(self._pass_field, "xpath")

    def getLoginButton(self):
        # return self.driver.find_element(By.XPATH, self._login_button)
        return self.getElement(self._login_button, "xpath")

    def clickSignInButton(self):
        self.getSignInField().click()

    def enterEmailField(self, userName):
        # self.getEmailField().send_keys(userName)
        self.enterInElement(self.getEmailField(), userName)

    def enterPassField(self, password):
        # self.getPassField().send_keys(password)
        self.enterInElement(self.getPassField(), password)

    def clickLoginButton(self):
        self.getLoginButton().click()


    def login(self, userName="", password=""):
        self.clickSignInButton()
        self.enterEmailField(userName)
        self.enterPassField(password)
        time.sleep(3)
        self.clickLoginButton()


    def verifyLoginSuccessful(self):
        result = self.isElementPresent(locatorType="CLASS_NAME", path="zl-navbar-rhs-img")
        return result

    def verifyLoginFailed(self):
        # result = self.isElementPresent(locatorType="XPATH", path="//span[contains(text(),'Your username or password is invalid. Please try again.')]")
        # result = self.isElementPresent(locatorType="CLASS_NAME", path="zl-navbar-rhs-img")
        result = self.isElementPresent(locatorType="XPATH", path="//div[@class='form-group has-error']/span")
        return result

    def verifyLoginPageTitle(self):
        self.verifyPageTitle('Google')
