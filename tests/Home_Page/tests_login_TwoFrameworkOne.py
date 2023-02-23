# method name should be start or end  from test   eg. test_abc()
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.Home_Page.logginPageClass_twoFrameworkOne import loginPageClass
import unittest
import pytest
import time

class Test_login(unittest.TestCase):
    # @pytest.mark.run(order=2)
    # def test_login(self):
    #     baseURL = "https://courses.letskodeit.com/"
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #
    #     driver.get(baseURL)
    #     # time.sleep(3)
    #     lp = loginPageClass(driver)
    #     lp.login("test@gmail.com", "abcabc")
    #
    #     re = lp.verifyLoginSuccessful()
    #     assert re == True
    #
    #     time.sleep(3)

    @pytest.mark.run(order=1)
    def test_loginFail(self):
        baseURL = "https://courses.letskodeit.com/"
        driver = webdriver.Chrome('C:/Users/Cloud Analogy/PycharmProjects/Project_One/venv/Scripts/chromedriver.exe')
        driver.maximize_window()

        driver.get(baseURL)
        # time.sleep(3)
        lp = loginPageClass(driver)
        lp.login("test@email.com", "abcabcaa")
        time.sleep(3)

        re = lp.verifyLoginFailed()
        assert re == True
        time.sleep(3)

# if __name__ == "__main__":
#     unittest.main(verbosity=2)

# a = login_tests()
# a.test_login()

