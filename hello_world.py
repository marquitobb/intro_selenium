import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # windows
        cls.driver = webdriver.Chrome(executable_path=r'C:\Users\Marco\Desktop\working_win\Python\Selenium\extension_win\chromedriver.exe')
        # mac os
        # cls.driver = webdriver.Chrome(executable_path='./extension_mac/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_hello_world(cls):
        driver = cls.driver
        driver.get('https://www.loropy.com/')

    def test_visit_wikipedia(cls):
        driver = cls.driver
        driver.get('https://www.wikipedia.org/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello_world_report'))