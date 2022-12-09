import time
import unittest
import pytest
from base.register_courses_pages import RegisterCoursesPage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidRegistration(self):
        time.sleep(3)
        self.courses.clickOnAllCoursesLnk()
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll()
        self.courses.enrollCourse(num="10", exp="1220", cvv="10")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                         "Enrollment Failed Verification")


