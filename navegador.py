"""
Este clase sirve para ver como automatizar un popup o mejor conocido como alert en javascript
"""

import unittest
from selenium import webdriver
from time import sleep

class NavigatorTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Marco\Desktop\working_win\Python\Selenium\extension_win\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://www.google.com.mx/")

    def test_browser_navigator(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('don chambitas')
        search_field.submit()

        driver.back()
        driver.implicitly_wait(9)
        driver.forward()
        driver.implicitly_wait(9)
        driver.refresh()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)