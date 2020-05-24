from selenium.webdriver.common.by import By


class MainPageLocators(object):
    CREATE_BUTTON = (By.CLASS_NAME, 'button-create')

    INPUT_FIELD = (By.CLASS_NAME, 'ifield')

    CREATE_BOX = (By.CLASS_NAME, 'create-box')

    ACTUAL_CREATE_BUTTON = (By.XPATH, '/html/body/div[@id="root"]/main/div/div/div/form/button')




