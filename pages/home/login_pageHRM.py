import json
import os
from time import sleep

from base.BasePage import BasePage
from base.BasePageHRM import BasePageHRM
from base.selenium_driver import SeleniumDriver



class LoginPageHRM(BasePageHRM):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        data = json.load(open("{}\..\data\input_data.json".format(os.getcwd()),"r"))
        self.hrm_page_data = data["hrm_login_page"]
        locators = json.load(open("{}\..\data\locators.json".format(os.getcwd()),"r"))
        self.hrm_locators = locators["hrm_login_page"]

    def enter_username(self, name):
        self.sendKeys(name, locator=self.hrm_locators["username"], locatorType="xpath")

    def enter_password(self, password):
        self.sendKeys(password, locator=self.hrm_locators["password"], locatorType="xpath")

    def click_login_button(self):
        self.elementClick(locator=self.hrm_locators["login_button"], locatorType="xpath")

    def login_HRM(self, user):
        username = self.hrm_page_data[user]["username"]
        password = self.hrm_page_data[user]["password"]
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_successful(self):
        sleep(3)
        return self.isElementPresent(self.hrm_locators["user_dropdown"], locatorType="xpath")
