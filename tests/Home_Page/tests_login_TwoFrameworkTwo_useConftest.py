# method name should be start or end  from test   eg. test_abc()
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.Home_Page.logginPageClass_twoFrameworkOne import loginPageClass
import unittest
import pytest
import time

@pytest.mark.usefixtures("setupDriver")
class Test_login(unittest.TestCase):
    @pytest.fixture(autouse = True)
    def classSetup(self, setupDriver):
        self.lp = loginPageClass(self.driver)


    @pytest.mark.run(order=2)
    def test_login(self):
        self.lp.login("juhi.rajput@cloudanalogy.com", "abcabc")
        re = self.lp.verifyLoginSuccessful()
        assert re == True

        time.sleep(3)

    @pytest.mark.run(order=1)
    def test_loginFail(self):
        self.lp.login("juhi.rajput@cloudanalogy.com", "abcabcaa")
        time.sleep(3)
        re = self.lp.verifyLoginFailed()
        assert re == True
        time.sleep(3)



