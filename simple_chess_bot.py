from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = '/home/ryansmane/webdrivers/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://lichess.org')

game_selector = driver.find_element_by_class_name('config_ai')
game_selector.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "modal-overlay"))
    )
    side_selector = driver.find_element_by_class_name('white')
    side_selector.click()
    ghost = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ghost"))
    )
    yOffset = ghost.size['height']
    actions = ActionChains(driver)
    actions.move_to_element(ghost)
    actions.move_by_offset(0, yOffset*6)
    for x in range(8):
        actions.click()
        actions.move_by_offset(0, -yOffset)
        actions.click()
        actions.move_by_offset(yOffset, yOffset)
        actions.pause(3)

    actions.perform()
    driver.quit()


except Exception as e: 
    print(e)
