import pytest
import unittest

from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.login_page = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.login_page.login("valid_user")
        assert True==self.login_page.verify_login_successful()
        # self.login_page.login("toma.dey.dutta@gmail.com", "Alak*1985")
        # result1 = self.login_page.verifyLoginTitle()
        # self.ts.mark(result1, "Title Verified")
        # result2 = self.login_page.verifyLoginSuccessful()
        # print("Status: ",result2)
        # self.ts.markFinal("test_validLogin", result2, "Login was successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.login_page.login("invalid_user")
        assert True == self.login_page.verify_login_successful()
        # self.login_page.login("toma.dey.dutta@gmail.com", "Alak*1986")
        # result = self.login_page.verifyLoginFailed()
        # result = self.login_page.verifyLoginSuccessful()
        # assert result==True
