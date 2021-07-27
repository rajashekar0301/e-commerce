from selenium import webdriver

class LoginPage:
    textbox_username_id='Email'
    textbox_password_id='Password'
    button_login_css="button[type='submit']"
    link_logout_linktext='Logout'

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)


    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element_by_css_selector(self.button_login_css).click()
        act_title = self.driver.title
        if act_title == 'Dashboard / nopCommerce administration':
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False

    def ClickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
