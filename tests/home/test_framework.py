from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def test(self):
        baseUrl = "https://id.atlassian.com/login"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        emailField = driver.find_element(By.NAME, "username")
        emailField.send_keys("leoalak@gmail.com")
        loginLink = driver.find_element(By.XPATH, "//button[@id='login-submit']//span[contains(text(),'Continue')]")
        loginLink.click()
        passwordField = driver.find_element(By.NAME, "password")
        passwordField.send_keys("TomaDutta*1996")
        loginLink1 = driver.find_element(By.XPATH, "//button[@id='login-submit']//span[contains(text(),'Log in')]")
        loginLink1.click()
              # emailField.clear()

        time.sleep(3)

        searchFi = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        searchFi.send_keys("abdd")
        time.sleep(4)
        driver.quit()



ff = ClickAndSendKeys()
ff.test()