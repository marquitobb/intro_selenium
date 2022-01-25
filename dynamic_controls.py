import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep

class DynamicControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Marco\Desktop\working_win\Python\Selenium\extension_win\chromedriver.exe')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Dynamic Controls').click()

    def test_name_elements(self):
        driver = self.driver

        checkbox = driver.find_element_by_xpath('//*[@id="checkbox"]')
        checkbox.click()

        remove_button = driver.find_element_by_xpath('//*[@id="checkbox-example"]/button')
        remove_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkbox-example"]/button')))
        remove_button.click()

        enable_disable_button = driver.find_element_by_xpath('//*[@id="input-example"]/button')
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/button')))

        text_area = driver.find_element_by_xpath('//*[@id="input-example"]/input')
        text_area.send_keys('Marco')

        enable_disable_button.click()


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)