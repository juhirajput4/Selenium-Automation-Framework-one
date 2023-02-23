from base.Selenium_driver import seleniumDriver

class basePage(seleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verifyPageTitle(self, title):
        if title in self.getTitle():
            return True
        else:
            return False
