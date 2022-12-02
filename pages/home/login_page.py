from base.BasePage import BasePage
from base.selenium_driver import SeleniumDriver
import time


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _login_link = "//a[normalize-space()='Sign In']"#//a[contains(text(),'Login')]"
    _email_field = "//form[@role='form']//input[@id='email']"#"username"
    _password_field = "//input[@id='password']"#password"
    _login_button = "//input[@value='Login']"#//button[@id='login-submit']//span[contains(text(),'Log in')]"
    _home_icon = "//a[normalize-space()='Home']"
    _continueBtn = "//button[@id='login-submit']//span[contains(text(),'Continue')]"
    _search_box = "//input[@placeholder='Search']"

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box)

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def clickContinueBtn(self):
        self.elementClick(self._continueBtn, locatorType="xpath")

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passField = self.getElement(locator=self._password_field)
        passField.clear()

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def clickHomeIcon(self):
        self.elementClick(self._home_icon, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        # self.clearFields()
        self.enterEmail(email)
        #self.clickContinueBtn()
        self.enterPassword(password)
        self.clickLoginButton()


    def verifyLoginSuccessful(self):
        time.sleep(4)
        result = self.isElementPresent(self._home_icon,
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[@class='text-with-icon']",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Rahul Shetty Academy")
        # if "Rahul Shetty Academy" in self.getTitle():
        #     return True
        # else:
        #     return False
