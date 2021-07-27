import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import time

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_customer_add_003:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    @pytest.mark.user
    def test_add_new_customer(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # Create Object of LoginPage Class and calling driver, as it constructor in LoginPage Clas
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.customer = AddCustomer(self.driver)
        self.customer.customer_main_menu()
        self.customer.customer_sub_menu()
        customer_email = self.customer.customer_email()
        self.customer.enter_first_name()
        self.customer.enter_last_name()
        self.customer.save_customer()
        self.customer.search_email_address(customer_email)
        self.customer.button_search()





