from selenium.webdriver.common.by import By


class Login_Admin_Page:
    userName_id="Email"
    password_id="Password"
    loginButton_XPath="//button[@type='submit']"
    logout_LinkText = "Logout"


    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(By.ID, self.userName_id).clear()
        self.driver.find_element(By.ID, self.userName_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.loginButton_XPath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.logout_LinkText).click()