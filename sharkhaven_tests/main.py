import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import page

PATH = '/home/ryansmane/webdrivers/chromedriver'

class SharkHavenCreateRoom(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://ryansmane.github.io/war-client/")
    
    def test_title(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "Sharkhaven not in title."

    def test_create_lobby_in_SharkHaven(self):
        NAME_TO_TEST = 'Test Room'
        main_page = page.MainPage(self.driver)
        main_page.click_create_button()
        assert main_page.input_field_appears(), "Input field does not appear."
        main_page.room_name_input = NAME_TO_TEST
        main_page.create_room_click()
        self.driver.execute_script("window.open('https://ryansmane.github.io/war-client/','new');")
        assert main_page.room_appeared(NAME_TO_TEST), "Room Not Created"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
