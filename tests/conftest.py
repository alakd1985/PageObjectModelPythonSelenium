import json
import pytest

from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage



@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    web_driver_factory = WebDriverFactory(browser)
    data = json.load(open("..\data\input_data.json", "r"))
    driver = web_driver_factory.get_webdriver_instance(url=data["base_url"])
    # wdf = WebDriverFactory(browser)
    # driver = wdf.getWebDriverInstance()
    # lp = LoginPage(driver)
    # lp.login("toma.dey.dutta@gmail.com", "Alak*1985")
    #lp.login("leoalak@gmail.com", "TomaDutta*1996")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    #driver.quit()
    print("Running one time tearDown")

@pytest.yield_fixture()
def setUpHRM():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUpHRM(request, browser):
    print("Running one time setUp")
    web_driver_factory = WebDriverFactory(browser)
    data = json.load(open("..\data\input_data.json","r"))
    driver = web_driver_factory.get_webdriver_instance(url=data["hrm_url"])

    # # wdf1 = WebDriverFactoryHRM(browser)
    # # driver = wdf1.getWebDriverInstanceHRM()
    # lp1 = LoginPageHRM(driver)
    # lp1.loginHRM("Admin", "admin123")


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
