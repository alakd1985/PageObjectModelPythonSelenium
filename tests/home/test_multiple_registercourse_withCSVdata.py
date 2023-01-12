import time
import unittest
import pytest
from base.register_courses_pages import RegisterCoursesPage
from ddt import ddt, data, unpack
from utilities.teststatus import TestStatus
from utilities.readData import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterMultipleCoursesTestsWithCSVData(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Volumes/Alak/Dutta/Python Selenium/PageObjectModelPythonSelenium/utilities/testdata.csv"))
    @unpack
    def test_invalidRegistration(self, courseName, ccNum, ccExp, ccCVV):
        time.sleep(3)
        self.courses.clickOnAllCoursesLnk()
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll()
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                         "Your card number is incomplete.")
        self.courses.clickOnAllCoursesLnk()


