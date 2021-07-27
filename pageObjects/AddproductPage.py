from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from pageObjects.pg_utils import date
from selenium.webdriver.support.ui import Select


class AddProduct:

    catalog_menu = "//a[@href='#']//p[contains(text(),'Catalog')]"
    products_sub_menu = "//a[@href='/Admin/Product/List']//p[contains(text(),' Products')]"
    Add_product = "//a[normalize-space()='Add new']"
    prod_name ='Name'
    categories = "(//div[@role='listbox']//parent::div)[1]"
    tag ="//div[normalize-space()='Enter tags ...']"
    GST = "//input[@id='Gtin']"


    def __init__(self,driver):
        self.driver=driver

    def catalog_main_menu(self):
        time.sleep(4)
        self.driver.find_element_by_xpath(self.catalog_menu).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.products_sub_menu).click()

    def add_new_product(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.Add_product).click()

    def category_selection(self):

        # self.driver.execute_script("window.scrollTo(0, 480)")
        self.driver.find_element_by_xpath(self.categories).click()
        element1 = self.driver.find_element_by_xpath("//li[normalize-space()='Computers >> Desktops']")
        element2 = self.driver.find_element_by_xpath("//li[normalize-space()='Computers >> Notebooks']")
        action = ActionChains(self.driver)
        action.move_to_element(element1)
        action.click()
        action.perform()
        time.sleep(2)
        action1 = ActionChains(self.driver)
        action1.move_to_element(element2)
        action1.click()
        action1.perform()
        time.sleep(2)
        action1.send_keys(Keys.TAB)
        # ActionChains(self.driver).key_down(Keys.CONTROL).click(element1).key_up(Keys.CONTROL).perform()
        #
        # ActionChains(self.driver).key_down(Keys.CONTROL).click(element2).key_up(Keys.CONTROL).perform()
    def product_tags(self):

        time.sleep(5)
        tag1 = self.driver.find_element_by_xpath(self.tag)
        action =ActionChains(self.driver)
        action.click(tag1)
        action.send_keys("Test")
        action.perform()
        action.send_keys(Keys.TAB)

    def product_name(self):

        product_name =self.driver.find_element_by_id(self.prod_name)
        product_name.send_keys("Product" + date.date_timestamp(1))

    def GTIN(self):
        self.driver.find_element_by_xpath(self.GST).send_keys("32SDFT52FTG587")

    def save_product(self):
        self.driver.find_element_by_name('save').click()
        time.sleep(2)
        sucess_text = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable']").text
        print(sucess_text)
        sucess_text = self.driver.find_element_by_xpath(
            "//div[@class='alert alert-success alert-dismissable']//button").click()




















