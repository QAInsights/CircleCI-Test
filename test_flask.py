import sys
from datetime import datetime
import pytest
from selenium import webdriver
import time


@pytest.mark.nondestructive
def test_nondestructive(selenium):
    options = webdriver.FirefoxOptions()
    options.add_argument("headless")
    options.headless = True

    driver = webdriver.Firefox(executable_path="geckodriver.exe", options=options)
    try:
        driver.get('http://localhost:5000')
        selenium.implicitly_wait(10)
        while True:
            actual_date_time = driver.find_elements_by_xpath("//p[@id='time']")[0].text
            print("Actual", actual_date_time)
            python_button = driver.find_elements_by_xpath("//button[@id='submit']")[0]
            python_button.click()

            new_date_time = driver.find_elements_by_xpath("//p[@id='time']")[0].text
            print("New", new_date_time)
            if actual_date_time == new_date_time:
                python_button.click()
            else:
                break
        driver.quit()
    finally:
        driver.quit()
