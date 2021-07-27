from selenium import webdriver
import time
from pageObjects.pg_utils import date
from testCases.conftest import setup


class AddCustomer:

    # Add Customer Page
    #lnkCustomers_menu_link = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menu_link = "//a[@href='#']//p[contains(text(),'Catalog')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtCustomerRoles_xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable']"
    lstitem_Administrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitem_Guests_xpath = "//li[contains(text(),'Guests')]"
    lstitem_Vendros_xpath = "//li[contains(text(),'Vendors')]"
    lstitem_ForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"
    email_search ="//input[@id='SearchEmail']"
    search_buttn ="//button[normalize-space()='Search']"


    def __init__(self,driver):
        self.driver=driver

    def customer_main_menu(self):
        time.sleep(4)
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_link).click()
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def customer_sub_menu(self):

        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def customer_email(self):
        email = self.driver.find_element_by_xpath(self.txtEmail_xpath)
        email.send_keys(date.date_timestamp(1)+'@demo.com')
        value =self.driver.find_element_by_xpath(self.txtEmail_xpath).get_attribute("value")

        print("Email is : "+str(value))
        return value
    def enter_first_name(self):
        email = self.driver.find_element_by_xpath(self.txtFirstName_xpath)
        email.send_keys("Fname")

    def enter_last_name(self):
        email = self.driver.find_element_by_xpath(self.txtLastName_xpath)
        email.send_keys("Lname")

    def save_customer(self):

        self.driver.find_element_by_xpath(self.btnSave_xpath).click()

    def search_email_address(self,customer_email):
        email = self.driver.find_element_by_xpath(self.email_search)
        email.send_keys(customer_email)

    def button_search(self):
        self.driver.find_element_by_xpath(self.search_buttn).click()





