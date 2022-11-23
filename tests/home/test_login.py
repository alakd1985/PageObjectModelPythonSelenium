import pytest
from pages.home.login_page import LoginPage
import unittest
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("toma.dey.dutta@gmail.com", "Alak*1985")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verified")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("toma.dey.dutta@gmail.com", "Alak*1986")
        result = self.lp.verifyLoginFailed()
        assert result == True
