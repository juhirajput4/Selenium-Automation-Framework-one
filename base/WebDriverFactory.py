from selenium import webdriver

class WebdriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def getWebdriverInstance(self):
        baseURL = "https://courses.letskodeit.com/"
        if self.browser == "chrome":
            driver = webdriver.Chrome("C:/Users/Cloud Analogy/PycharmProjects/Project_One/venv/Scripts/chromedriver.exe")
        else:
            driver = webdriver.Edge()
        driver.maximize_window()
        driver.get(baseURL)
        return driver
