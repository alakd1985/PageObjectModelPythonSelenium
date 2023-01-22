import pytest
import unittest
from pages.home.login_pageHRM import LoginPageHRM
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUpHRM", "setUpHRM")
class LoginTestsHRM(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUpHRM):
        self.lp = LoginPageHRM(self.driver)
        self.ts = TestStatus(self.driver)
    @pytest.mark.run(order=1)
    def test_validLoginHRM(self):
        self.lp.loginHRM("Admin", "admin123")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verified")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")

    # @pytest.mark.run(order=1)
    # def test_invalidLogin(self):
    #     self.lp.login("toma.dey.dutta@gmail.com", "Alak*1986")
    #     result = self.lp.verifyLoginFailed()
    #     assert result == True
