from base.BasePage import BasePage
from base.BasePageHRM import BasePageHRM
from base.selenium_driver import SeleniumDriver
import time


class LoginPageHRM(BasePageHRM):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _userName = "//input[@placeholder='Username']"
    _password = "//input[@placeholder='Password']"
    _loginBtn = "//button[normalize-space()='Login']"


    def enterUserName(self, name):
        self.sendKeys(name, locator=self._userName, locatorType="xpath")

    def enterUserPassword(self, password):
        self.sendKeys(password, locator=self._password, locatorType="xpath")

    def clickLoginBtn(self):
        self.elementClick(self._loginBtn, locatorType="xpath")

    def loginHRM(self, username="", password=""):
        self.enterUserName(username)
        self.enterPassword(password)
        self.clickLoginButton()



