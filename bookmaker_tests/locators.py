from selenium.webdriver.common.by import By


class DashboardLocators(object):
    
    LOGIN_BUTTON = (By.LINK_TEXT, 'Login')

class LoginPageLocators(object):

    LOGIN_BUTTON = (By.CLASS_NAME, 'login-button')
