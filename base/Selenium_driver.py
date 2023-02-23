import os
from traceback import print_stack

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities import customLogger_twoFrameworkOne as cl
import logging


class seleniumDriver():

    log = cl.CustomLogger(loggerName="classLogger", logLevel=logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower() # iD => id / ID => id / Id => id
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'class_name':
            return By.CLASS_NAME
        else :
            return False

    def getElement(self,path, locatorType):
        element = None
        try:
            self.driver.implicitly_wait(10)
            byType = self.getByType(locatorType)

            element = self.driver.find_element(byType,path)
            self.log.info("Element found with locator: " + path +
                          " and  locatorType: " + locatorType)

        except:
            self.log.info("Element not found with locator: " + path +
                          " and  locatorType: " + locatorType)
        return element
        time.sleep(2)

    def enterInElement(self,element, text):
        element.send_keys(text)

    def clickElement(self, path, locatorType):
        self.getElement(path, locatorType).click()

    def isElementPresent(self, locatorType, path):
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,path)
            if element is not None:
                print("element found")
                return True
            else:
                print("element not found")
                return False

        except:
            print("in exception element not found")
            return False

    def Screenshot(self, resultMessage):
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativePath = screenshotDirectory + fileName
        currntDirectry = os.path.dirname(__file__)
        destinationFile = os.path.join(currntDirectry, relativePath)
        destinationDirectory = os.path.join(currntDirectry, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)

        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()







