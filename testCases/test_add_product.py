import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import time


from pageObjects.AddproductPage import AddProduct
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_customer_add_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    @pytest.mark.user
    def test_add_new_product(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # Create Object of LoginPage Class and calling driver, as it constructor in LoginPage Clas
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.customer = AddProduct(self.driver)
        self.customer.catalog_main_menu()
        self.customer.add_new_product()
        self.customer.product_name()
        self.customer.category_selection()
        self.customer.product_tags()
        self.customer.GTIN()
        self.customer.save_product()













