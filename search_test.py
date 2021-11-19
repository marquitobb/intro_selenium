import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):

    def setUp(self):
        # windows
        # self.driver = webdriver.Chrome(executable_path=r'C:\Users\Marco\Desktop\working_win\Python\Selenium\chromedriver.exe')
        # mac os
        self.driver = webdriver.Chrome(executable_path='./extension_mac/chromedriver')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id('search')

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name('q')

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name('input-text')

    def test_search_button_enabled(self):
        search_button = self.driver.find_element_by_class_name('button')

    # def test_count_of_promo_banner_images(self):
    #     banner_list = self.driver.find_elements_by_class_name('promos')
    #     banners = banner_list.find_elements_by_tag_name('img')
    #     self.assertEqual(3, len(banners))

    # def test_vip_promo(self):
    #     vip_promo = self.driver.find_element_by_xpath('//*[@id="promo_banner_left"]/div/div/div/div/a/img')

    def test_shopping_cart_button(self):
        shopping_cart_button = self.driver.find_element_by_css_selector('div.header-minicart span.icon')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)