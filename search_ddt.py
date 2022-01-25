import unittest
from selenium import webdriver
from ddt import ddt, data, unpack
from time import sleep

@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Marco\Desktop\working_win\Python\Selenium\extension_win\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
        # driver.find_element_by_link_text('Sortable Data Tables').click()

    @data(('dress', 6), ('music', 6))
    @unpack
    def test_search_name(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        print(f'found {len(products)} products')

        for product in products:
            print(product.text)

        self.assertEqual(expected_count, len(products))


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)