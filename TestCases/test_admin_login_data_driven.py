from datetime import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v137.dom_storage import clear

from Pages.LoginAdminPage import Login_Admin_Page
from TestCases.conftest import browser, setup
from utilities.read_properties import Read_config
from utilities.loggerTest import Log_Maker
from utilities import excel_utils

class Test_02_Admin_Login:
    admin_page_url = Read_config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = ".//TestData//test_Data.xlsx"
    status_list =[]

    def test_valid_login_data_driven(self, setup):
        self.logger.info("******************Valid Login Data Driven Verification*********************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_login = Login_Admin_Page(self.driver)
        self.rows=excel_utils.get_row_count(self.path,"Sheet1")
        print("num of rows", self.rows)
        for r in range(2,self.rows+1):
            self.username = excel_utils.read_data(self.path,"Sheet1",r,1)
            self.password = excel_utils.read_data(self.path, "Sheet1", r, 2)
            self.exp_result = excel_utils.read_data(self.path, "Sheet1", r, 3)
            self.admin_login.enter_username(self.username)
            self.admin_login.enter_password(self.password)
            self.admin_login.click_login()
            self.driver.implicitly_wait(10)
            act_Dashboard_txt = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_Dashboard_txt == exp_title:
                if self.exp_result == "Yes":
                    self.logger.info("******************Test data passed*********************")
                    self.status_list.append("Pass")
                    self.admin_login.click_logout()
                elif self.exp_result == "No":
                    self.logger.info("******************Test data failed*********************")
                    self.status_list.append("Fail")
                    self.admin_login.click_logout()
            elif act_Dashboard_txt != exp_title:
                if self.exp_result == "Yes":
                    self.logger.info("******************Test data failed*********************")
                    self.status_list.append("Fail")
                elif self.exp_result == "No":
                    self.logger.info("******************Test data Passed*********************")
                    self.status_list.append("Pass")

        print("Status", self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("Test Admin data driven test is failed")
            assert False
        else:
            self.logger.info("Test Admin data driven test is pass")
            assert True

