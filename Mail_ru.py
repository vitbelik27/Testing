import unittest
from selenium import webdriver

class OpenMailRuPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_logIn(self):
        driver = self.driver
        driver.get('https://mail.ru')
        assert 'Mail.Ru' in driver.title
        driver.find_element_by_id('mailbox__login').send_keys('vitbelik')
        driver.find_element_by_id('mailbox__password').send_keys('011235813Baqu')
        driver.find_element_by_id('mailbox__auth__button').click()
        driver.implicitly_wait(1000)
        username = driver.find_element_by_id('PH_user-email').get_attribute('text')
        print(username)

    #def tearDown(self):
    #    self.driver.quit()

if __name__ == "__main__":
    unittest.main()