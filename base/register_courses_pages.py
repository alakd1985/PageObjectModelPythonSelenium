import utilities.custom_logger as cl
import logging
import time
from base.BasePage import BasePage
class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    _search_box = "//input[@id='search']"
    _course = "//img[@alt='course image']"#"//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _all_courses = "//a[normalize-space()='ALL COURSES']"
    _enroll_button = "enroll-button-top"
    _enroll_in_course = "//button[normalize-space()='Enroll in Course']"
    _cc_num = "cardnumber"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _submit_enroll = "//div[@id='new_card']//button[contains(text(),'Enroll in Course')]"
    _enroll_error_message = "//div[@id='new_card']//div[contains(text(),'The card number is not a valid credit card number.')]"

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box,locatorType="xpath")

    def selectCourseToEnroll(self):
        self.elementClick(locator=self._course, locatorType="xpath")
    def clickOnEnrollCourseLnk(self):
        self.elementClick(locator=self._enroll_in_course, locatorType="xpath")
    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button)
    def clickOnAllCoursesLnk(self):
        self.elementClick(locator=self._all_courses, locatorType="xpath")
    # def enterCardNum(self, num):
    #     self.sendKeys(num, locator=self._cc_num)

    # def enterCardExp(self, exp):
    #     self.sendKeys(exp, locator=self._cc_exp)

    # def enterCardCVV(self, cvv):
    #     self.sendKeys(cvv, locator=self._cc_cvv)

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCardNum(self, num):
        # This frame takes at least 6 seconds to show, it may take more for you
        time.sleep(6)
        # self.switchToFrame(name="__privateStripeFrame8") this is problem
        self.SwitchFrameByIndex(self._cc_num, locatorType="name")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType="name")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        # self.switchToFrame(name="__privateStripeFrame9")
        self.SwitchFrameByIndex(self._cc_exp, locatorType="name")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        # self.switchToFrame(name="__privateStripeFrame10")
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="name")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
        self.switchToDefaultContent()

    def enterZip(self, zip):
        # self.switchToFrame(name="__privateStripeFrame11")
        self.SwitchFrameByIndex(self._zip, locatorType="name")
        self.sendKeys(zip, locator=self._zip, locatorType="name")
        self.switchToDefaultContent()
    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollCourseLnk()
        #self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result
