# method name should be start or end  from test   eg. test_abc()
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.Home_Page.loginPageClass import loginPageClass
import unittest
import time

class login_tests(unittest.TestCase):
    def test_login(self):
        baseURL = "https://courses.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(baseURL)
        # time.sleep(3)
        lp = loginPageClass(driver)
        lp.login("test@gmail.com", "abcabc")

        userIcon = driver.find_element(By.CLASS_NAME,"zl-navbar-rhs-img ")
        if userIcon is not None:
            print("login successful")
        else:
            print("not able to login")

        time.sleep(3)

# if __name__ == "__main__":
#     unittest.main(verbosity=2)

# a = login_tests()
# a.test_login()

