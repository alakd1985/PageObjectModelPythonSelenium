import pytest
import unittest
from pages.home.login_pageHRM import LoginPageHRM
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUpHRM", "setUpHRM")
class LoginTestsHRM(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUpHRM): #class_setup
        self.login_page_hrm = LoginPageHRM(self.driver)
        self.test_status = TestStatus(self.driver)
    @pytest.mark.run(order=1)
    def test_valid_login_HRM(self):
        self.login_page_hrm.login_HRM("valid_user")
        assert True == self.login_page_hrm.verify_login_successful()
        # result = self.login_page_hrm.verify_login_successful()
        # assert True== result
        # self.test_status.markFinal(__name__, result, )
        # import pdb;pdb.set_trace()
        # self.login_page_hrm.login_HRM("Admin", "admin123")
        # result1 = self.login_page_hrm.verifyLoginTitle()
        # self.test_status.mark(result1, "Title Verified")
        # result2 = self.login_page_hrm.verifyLoginSuccessful()
        # self.test_status.markFinal("test_validLogin", result2, "Login was successful")

    # @pytest.mark.run(order=1)
    # def test_invalidLogin(self):
    #     self.lp.login("toma.dey.dutta@gmail.com", "Alak*1986")
    #     result = self.lp.verifyLoginFailed()
    #     assert result == True
