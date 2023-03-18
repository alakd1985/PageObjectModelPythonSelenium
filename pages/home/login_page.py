import json
import os
import time

from base.BasePage import BasePage
from base.selenium_driver import SeleniumDriver

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        print("{}\data\input_data.json".format(os.getcwd()))
        data = json.load(open("{}\..\data\input_data.json".format(os.getcwd()), "r"))
        self.login_data = data["login_page"]
        locators = json.load(open("{}\..\data\locators.json".format(os.getcwd()), "r"))
        self.login_locators = locators["login_page"]

    def enter_course_name(self, name):
        self.sendKeys(name, locator=self.login_locators["search_box"])

    def click_login_link(self):
        self.elementClick(self.login_locators["login_link"], locatorType="xpath")


    def click_continue_button(self):
        self.elementClick(self.login_locators["continueBtn"], locatorType="xpath")

    def clear_fields(self):
        emailField = self.getElement(locator=self.login_locators["email_field"])
        emailField.clear()
        passField = self.getElement(locator=self.login_locators["password_field"])
        passField.clear()

    def enter_email(self, email):
        self.sendKeys(email, self.login_locators["email_field"], locatorType="xpath")

    def enter_password(self, password):
        self.sendKeys(password, self.login_locators["password_field"], locatorType="xpath")

    def click_login_button(self):
        self.elementClick(self.login_locators["login_button"], locatorType="xpath")

    def click_home_icon(self):
        self.elementClick(self.login_locatorshome_icon, locatorType="xpath")

    def login(self, user):
        username = self.login_data[user]["username"]
        password = self.login_data[user]["password"]
        self.click_login_link()
        self.enter_email(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_successful(self):
        time.sleep(4)
        return self.isElementPresent(self.login_locators["home_icon"], locatorType="xpath")

    def verifyLoginFailed(self):
        return self.isElementPresent(self.login_locators["verify_login"], locatorType="xpath")

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Rahul Shetty Academy")
        # if "Rahul Shetty Academy" in self.getTitle():
        #     return True
        # else:
        #     return False
