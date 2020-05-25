import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import page

PATH = '/home/ryansmane/webdrivers/chromedriver'


class BookmakerDashboard(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://warm-basin-48507.herokuapp.com")

    def test_title(self):
        dashboard = page.Dashboard(self.driver)
        assert dashboard.about_at_home(), "No About Section."
    
    def test_login_redirect(self):
        dashboard = page.Dashboard(self.driver)
        dashboard.go_to_login()
        assert 'Email Address' in self.driver.page_source, 'Login not found on login page'


    def tearDown(self):
        self.driver.close()

class BookmakerLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://warm-basin-48507.herokuapp.com/login")

    def test_login(self):
        login_page = page.LoginPage(self.driver)
        login_page.email_input = 'testauthor123@gmail.com'
        login_page.password_input = 'Have A Nice Day'
        login_page.login()
        actions = ActionChains(self.driver)
        actions.pause(3)
        actions.perform()
        assert "Literary Agencies" in self.driver.page_source, "No Redirect Occured"


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
