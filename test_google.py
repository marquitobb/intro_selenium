import unittest
from selenium import webdriver
from time import sleep
from google_page import GooglePage

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path = r'C:\Users\Marco\Desktop\working_win\Python\Selenium\extension_win\chromedriver.exe')
        driver = cls.driver
        driver.get('https://the-internet.herokuapp.com/')

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)


    @classmethod
    def tearDown(cls):
        driver = cls.driver
        driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)