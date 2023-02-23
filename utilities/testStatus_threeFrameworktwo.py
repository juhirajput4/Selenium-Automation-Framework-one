from base.Selenium_driver import seleniumDriver
from utilities import customLogger_twoFrameworkOne as cl
import logging

class testStatus(seleniumDriver):
    log = cl.CustomLogger(loggerName="testStatus", logLevel=logging.DEBUG)

    def __init__(self, driver):

        super().__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        if result:
            self.resultList.append("Pass")
            self.log.info("Verification successful: "+ resultMessage)
        else:
            self.resultList.append("Fail")
            self.Screenshot(resultMessage)
            self.log.error("Verification failed: "+ resultMessage)

    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage ):
        self.setResult(result, resultMessage)

        if "Fail" in self.resultList:
            self.log.error(testName + "Test Failed")
            self.resultList.clear()
            assert True == False
        else:
            self.log.error(testName + "Test Pass")
            self.resultList.clear()
            assert True == True





