import unittest
from selenium import webdriver
from time import sleep

class Tables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Marco\Desktop\working_win\Python\Selenium\extension_win\chromedriver.exe')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_name_elements(self):
        driver = self.driver

        table_data = [[] for i in range(5)]
        print(table_data)

        for i in range(5):
            header = driver.find_element_by_xpath('//*[@id="table1"]/thead/tr/th[{}]/span'.format(i+1))
            table_data[i].append(header.text)

            for j in range(4):
                row_data = driver.find_element_by_xpath('//*[@id="table1"]/tbody/tr[{}]/td[{}]'.format(j+1, j+1))
                table_data[i].append(row_data.text)

        print(table_data)



    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)