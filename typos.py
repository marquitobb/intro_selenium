import unittest
from selenium import webdriver
from time import sleep

class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Marco\Desktop\working_win\Python\Selenium\extension_win\chromedriver.exe')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Typos').click()

    def test_name_elements(self):
        driver = self.driver

        paragraph_to_check = driver.find_element_by_xpath('//*[@id="content"]/div/p[2]')
        paragraph_to_check_text = paragraph_to_check.text
        print(f'Text: {paragraph_to_check_text}')

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while paragraph_to_check_text != correct_text:
            paragraph_to_check = driver.find_element_by_xpath('//*[@id="content"]/div/p[2]')
            paragraph_to_check_text = paragraph_to_check.text
            driver.refresh()

        while not found:
            if paragraph_to_check_text == correct_text:
                tries += 1
                driver.refresh()
                found = True

        self.assertEqual(found, True)

        print(f'Tries: {tries}')



    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)