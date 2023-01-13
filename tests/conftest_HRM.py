import pytest
from base.webdriverfactory_HRM import WebDriverFactoryHRM
from pages.home.login_pageHRM import LoginPageHRM


@pytest.yield_fixture()
def setUpHRM():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUpHRM(request, browser):
    print("Running one time setUp")
    wdf1 = WebDriverFactoryHRM(browser)
    driver = wdf1.getWebDriverInstanceHRM()
    lp1 = LoginPageHRM(driver)
    lp1.loginHRM("Admin", "admin123")


    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    #driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
