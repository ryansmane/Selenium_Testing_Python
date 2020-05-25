from element import BasePageElement
from locators import DashboardLocators, LoginPageLocators


class EmailText(BasePageElement):

    locator = 'formBasicEmail'


class PasswordText(BasePageElement):

    locator = 'formBasicPassword'


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class Dashboard(BasePage):

    def about_at_home(self):
        return "About" in self.driver.page_source

    def go_to_login(self):
        login_button = self.driver.find_element(*DashboardLocators.LOGIN_BUTTON)
        login_button.click()
    
    def email_field_present(self):
        return 'Email Address' in self.driver.page_source

class LoginPage(BasePage):
    
    email_input = EmailText()
    password_input = PasswordText()

    def login(self):
        login_button = self.driver.find_element(
            *LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def agency_list_present(self):
        return "Literary Agencies" in self.driver.page_source
        
