import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"
    # Storing the value in logger variable , whatever return from LogGen.loggen (Class.method)
    logger = LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_ddt(self, setup):
        # Rather than direct defining Browser here, we can call Fixture from conftest.py
        # self.driver = WebDriver.Chrome()
        self.logger.info("********** Test_002_DDT_Logino*************")
        self.logger.info("********** Verifying Login Scenario*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        # Create Object of LoginPage Class and calling driver, as it constructor in LoginPage Clas
        self.lp = LoginPage(self.driver)

        # Get total number of rows from excel, by passing file path and sheet name
        self.rows=XLUtils.getRowCount(self.path,'Sheet')
        print('Number of rows in a Excel=',self.rows)

        lst_status=[]   # Empty list variable to store the result status

        # Using for loop to go to all data of excel, start from 2 as first will be consider as column
        # In python we have to pass rows+1, or else it will not read last cell value
        for r in range(2,self.rows+1):
            self.username = XLUtils.readData(self.path,'Sheet',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet',r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet',r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.ClickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            #Now will check if condition to check exp and act title
            if act_title==exp_title:
                #Here will check exp message of Excelsheet 3rd column value
                if self.exp=='Pass':
                    self.logger.info('***Passed***')
                    #Now user has to logout , so that loop can go for next set of value
                    self.lp.ClickLogout()
                    #Result of Success need to be appended to List variable
                    lst_status.append('Pass')
                elif self.exp=='Fail':
                    self.logger.info('***Failed***')
                    #Now user has to logout , so that loop can go for next set of value
                    self.lp.ClickLogout()
                    #Result of Success need to be appended to List variable
                    lst_status.append('Fail')

            elif act_title !=exp_title:
                #Here will check exp message of Excelsheet 3rd column value
                if self.exp=='Pass':
                    self.logger.info('***Failed***')
                    #Result of Success need to be appended to List variable
                    lst_status.append('Fail')
                elif self.exp=='Fail':
                    self.logger.info('***Passed***')
                    #Result of Success need to be appended to List variable
                    lst_status.append('Pass')

        #Now we need to check lst_status variable should not contain any Fail status
        if "Fail" not in lst_status:
            self.logger.info("****Login DDT Test Case Successful*****")
            self.driver.quit()
            assert True
        else:
            self.logger.info("****Login DDT Test Case Un-Successful*****")
            self.driver.close()
            assert False

        self.logger.info("********** End of DDT Test*************")
        self.logger.info("********** Completed Test_002_DDT_Login*************")