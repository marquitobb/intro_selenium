import unittest
from selenium import webdriver
from time import sleep

class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Marco\Desktop\working_win\Python\Selenium\extension_win\chromedriver.exe')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Disappearing Elements').click()

    def test_name_elements(self):
        driver = self.driver

        options= []
        menu = 5
        tries = 1

        while len(options) < 5:
            options.clear()

            for i in range(menu):
                try:
                    option_name = driver.find_element_by_xpath('//*[@id="content"]/div/ul/li[{}]/a'.format(i+1))
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f'no option {i+1} is not found')
                    tries += 1
                    driver.refresh()

        print(f'Tries: {tries}')


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)