import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Login_001:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        time.sleep(5)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    # @pytest.mark.sanity
    def test_login(self, setup):
        # Rather than direct defining Browser here, we can call Fixture from conftest.py
        # self.driver = WebDriver.Chrome()

        self.driver = setup
        self.driver.get(self.baseURL)
        # Create Object of LoginPage Class and calling driver, as it constructor in LoginPage Clas
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        act_title = self.driver.title
        if act_title == 'Dashboard / nopCommerce administration':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
