# method name should be start or end  from test   eg. test_abc()
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.Home_Page.logginPageClass_threeFrameworkThree_UsingBasePage import loginPageClass
from utilities.testStatus_threeFrameworktwo import testStatus
import unittest
import pytest
import time

@pytest.mark.usefixtures("setupDriver")
class Test_login(unittest.TestCase):
    @pytest.fixture(autouse = True)
    def classSetup(self, setupDriver):
        self.lp = loginPageClass(self.driver)
        self.ts = testStatus(self.driver)


    @pytest.mark.run(order=2)
    def test_login(self):
        self.lp.login("juhi.rajput@cloudanalogy.com", "abcabc")


        time.sleep(3)
        re1 = self.lp.verifyLoginPageTitle()
        self.ts.mark(re1, "Title is not correct")
        re2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("login and title test", re2, "user icon verified")



        time.sleep(3)

    # @pytest.mark.run(order=1)
    # def test_loginFail(self):
    #     self.lp.login("juhi.rajput@cloudanalogy.com", "abcabcaa")
    #     time.sleep(3)
    #     re = self.lp.verifyLoginFailed()
    #     assert re == True
    #     time.sleep(3)



