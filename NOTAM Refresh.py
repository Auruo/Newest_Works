from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
def run_script():
    global driver
    url = 'https://notams.aim.faa.gov/notamSearch/nsapp.html#/'
    driver.get(url)

    time.sleep(2)

    if driver.current_url != url:
        
        read_and_understood_button = driver.find_element(By.CSS_SELECTOR, ".btn-info")
        
        read_and_understood_button.click()

    time.sleep(1)
    search_box = driver.find_element(By.NAME, "designatorsForLocation")

    search_box.send_keys('WVL')  
    search_box.send_keys(Keys.RETURN)

    time.sleep(60)
    driver.refresh()
    time.sleep(1)
    run_script()

run_script()