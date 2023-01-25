from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class seleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower() # iD => id / ID => id / Id => id
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'name':
            return By.NAME
        else :
            return False

    def getElement(self,path, locatorType):
        element = None
        try:
            self.driver.implicitly_wait(10)
            byType = self.getByType(locatorType)

            element = self.driver.find_element(byType,path)
            print('Element Found')

        except:
            print('Element Not Found')
        return element
        time.sleep(2)

    def enterInElement(self,element, text):
        element.send_keys(text)

    def clickElement(self, path, locatorType):
        self.getElement(path, locatorType).click()

    

