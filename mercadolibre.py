import unittest
from selenium import webdriver
from time import sleep

class MercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Marco\Desktop\working_win\Python\Selenium\extension_win\chromedriver.exe')
        driver = self.driver
        driver.get('https://mercadolibre.com/')

    def test_name_elements(self):
        driver = self.driver
        
        country = driver.find_element_by_xpath('//*[@id="CO"]')
        country.click()
        
        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        # TODO: fix this bogota bug
        location = driver.find_element_by_partial_link_text('Bogotá D.C.')
        location.click()
        sleep(3)

        # condition = driver.find_element_by_partial_link_text('Nuevo')
        # condition.click()
        # sleep(3)

        articles = []
        prices = []

        for i in range(5):
            articles_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/a/h2').text
            articles.append(articles_name)
            article_price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[3]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
            prices.append(article_price)

        print(articles)
        print(prices)


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)