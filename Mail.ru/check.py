from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest


class TestLogMailRu(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:\Pycharm\chromedriver.exe')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.login = 'first.student@mail.ru'
        cls.pasw = 'qwerty1A'

        cls.driver.get('https://mail.ru')
    """
    def setUp(self):
        self.driver = webdriver.Chrome('D:\Pycharm\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.login = 'first.student@mail.ru'
        self.pasw = 'qwerty1A'
    """
    def test_1_log_in(self):
        driver = self.driver
        login = self.login

        driver.find_element_by_xpath('//input[@id="mailbox__login"]').clean().send_keys(login)
        button = driver.find_element_by_id('mailbox__auth__button')
        button.click()

        #check the alert msg with without password
        alrt = driver.find_element_by_xpath("//div[@id='mailbox:authfail']").text
        err_text_without_pass = 'Введите пароль'
        #WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@id='mailbox:authfail']"), err_text_without_pass))
        self.assertEqual(alrt, err_text_without_pass)


    def test_2_inc_pasw(self):
        #few
        driver = self.driver
        login = self.login

        driver.find_element_by_xpath('//input[@id="mailbox__login"]').clean().send_keys(login)
        #check the alert msg with incorrect password
        driver.find_element_by_id('mailbox__password').send_keys('qwerty')
        button = driver.find_element_by_id('mailbox__auth__button')
        button.click()

        err_text_inc_pasw = 'Неверное имя или пароль'

        element = driver.find_element_by_xpath("//div[@id='mailbox:authfail']")
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@id='mailbox:authfail']"), err_text_inc_pasw))
        self.assertEqual(element.text, err_text_inc_pasw)

    def test_3_successfully(self):

        driver = self.driver
        login = self.login
        pasw = self.pasw

        driver.find_element_by_xpath('//input[@id="mailbox__login"]').send_keys(login)
        #CHECK that user can successfully log in
        driver.find_element_by_id('mailbox__password').clear()
        driver.find_element_by_id('mailbox__password').send_keys(pasw)
        button = driver.find_element_by_id('mailbox__auth__button')
        button.click()

        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//span/i[@id='PH_user-email']"), login))
        mail = driver.find_element_by_xpath("//span/i[@id='PH_user-email']").text
        self.assertEqual(mail, login)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    if __name__ == '__main__':
        unittest.main()
    """
    def tearDown(self):
        self.driver.quit()
    
if __name__ == '__main__':
    unittest.main()
    """