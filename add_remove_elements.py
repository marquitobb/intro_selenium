import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):
# extension_win\chromedriver.exe
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Marco\Desktop\working_win\Python\Selenium\extension_win\chromedriver.exe')
        driver = self.driver
        # driver.implicitly_wait(10)
        # driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements do you want to add? '))
        elements_removed = int(input('How many elements do you want to remove? '))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elements_added):
            add_button.click()
            # sleep(3)

        for i in range(elements_removed):
            try:
                remove_button = driver.find_element_by_xpath('//*[@id="elements"]/button')
                remove_button.click()
                # sleep(3)
            except:
                print('No more elements to remove')
                break

        if total_elements == 0:
            print('No elements left')
        else:
            print('Total elements left: {}'.format(total_elements))

        sleep(3)



    def tearDown(self):
        driver = self.driver
        # driver.implicitly_wait(3)
        driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)