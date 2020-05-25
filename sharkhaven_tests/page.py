from element import BasePageElement
from locators import MainPageLocators


class RoomNameTextElement(BasePageElement):

    locator = '/html/body/div[@id="root"]/main/div/div/div/form/div/input'


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    room_name_input = RoomNameTextElement()

    def is_title_matches(self):
        return "Shark Haven" in self.driver.title

    def click_create_button(self):
        button = self.driver.find_element(*MainPageLocators.CREATE_BUTTON)
        button.click()
    
    def input_field_appears(self):
        style = self.driver.find_element(*MainPageLocators.CREATE_BOX).get_attribute('style')
        return 'block' in style

    def create_room_click(self):
        button = self.driver.find_element(*MainPageLocators.ACTUAL_CREATE_BUTTON)
        button.click()

    def room_appeared(self, name):
        return f'Room Name: {name}' in self.driver.page_source


        

