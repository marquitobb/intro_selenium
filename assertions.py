import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

    def setUp(cls) -> None:
        # windows
        cls.driver = webdriver.Chrome(executable_path=r'C:\Users\Marco\Desktop\working_win\Python\Selenium\extension_win\chromedriver.exe')
        # mac os
        # cls.driver = webdriver.Chrome(executable_path='./extension_mac/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()


    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        # search_field.clear()
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.ID, 'search'))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity=2)