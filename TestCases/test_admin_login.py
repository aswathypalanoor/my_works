import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.LoginAdminPage import Login_Admin_Page
from TestCases.conftest import browser, setup
from TestCases.reusablecode import highlight_element_in_screenshot
from utilities.read_properties import Read_config
from utilities.loggerTest import Log_Maker

class Test_01_Admin_Login:
    admin_page_url = Read_config.get_admin_page_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    invalid_username = Read_config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def test_title_verification(self, setup):
        self.logger.info("******************Test_01_Admin_Login*********************")
        self.logger.info("******************Title Verification*********************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        if act_title == exp_title:
            self.logger.info("******************Title Matched*********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_title_verification.png")
            self.logger.info("******************Title Not Matched*********************")
            self.driver.close()
            assert False

    def test_valid_login(self, setup):
        self.logger.info("******************Valid Login Verification*********************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_login = Login_Admin_Page(self.driver)
        self.admin_login.enter_username(self.username)
        self.admin_login.enter_password(self.password)
        self.admin_login.click_login()
        dashboard_loc = "//div[@class='content-header']/h1"
        act_Dashboard_txt= self.driver.find_element(By.XPATH,dashboard_loc).text
        if act_Dashboard_txt == "Dashboard":
            self.logger.info("******************Logged in successfully*********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_valid_login.png")
            self.logger.info("******************Log in failed*********************")
            highlight_element_in_screenshot(self.driver, By.XPATH, dashboard_loc,
                                            screenshot_path=".\\Screenshots\\test_valid_login.png",
                                            output_path=".\\Screenshots\\test_valid_login.highlighted.png",
                                            color="red", border_width=3)
            self.driver.close()
            assert False


    def test_invalid_login(self, setup):
        self.logger.info("******************Invalid Login Verification*********************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_login = Login_Admin_Page(self.driver)
        self.admin_login.enter_username(self.invalid_username)
        self.admin_login.enter_password(self.password)
        self.admin_login.click_login()
        self.driver.implicitly_wait(20)
        error = "//div[@class='message-error validation-summary-errors']//li"
        error_message = self.driver.find_element(By.XPATH, error).text
        if error_message == "No error customer account found":
            self.logger.info("******************Verified the error message*********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_invalid_login1.png")
            self.logger.info("******************The error message not verified*********************")
            highlight_element_in_screenshot(self.driver, By.XPATH, error, screenshot_path=".\\Screenshots\\test_invalid_login1.png",
                                    output_path=".\\Screenshots\\test_invalid_login1.highlighted.png", color="red", border_width=3)
            self.driver.close()
            assert False