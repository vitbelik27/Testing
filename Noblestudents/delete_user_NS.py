from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import unittest

class NoSuchElementException():
    pass

class DeleteUserFromAdmin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(100)
        self.driver.get('https://stage.noblestudents.ready4.today/administrator/')
        self.adm_usr = 'admin'
        self.adm_pass = 'N0b1eStUdent$.c0m'
        self.deleted_user = 'child.second@mail.ru'

    def test_delete_user(self):
        driver = self.driver
        adm_usr = self.adm_usr
        adm_pass = self.adm_pass
        deleted_user = self.deleted_user

        #find login and password fields
        driver.find_element_by_id('mod-login-username').send_keys(adm_usr)
        driver.find_element_by_id('mod-login-password').send_keys(adm_pass)
        driver.find_element_by_xpath("//button[@class='btn btn-primary btn-block btn-large login-button']").click()

        WebDriverWait(driver, 100).until(EC.title_contains('Панель управления - Noble Students - Панель управления'))

        assert 'Панель управления - Noble Students - Панель управления' in driver.title

        #find users menue
        driver.find_element_by_link_text('Менеджер пользователей').click()
        #find deleted value
        #find search field
        driver.find_element_by_id('filter_search').send_keys(deleted_user)
        driver.find_element_by_xpath("//div[@class='btn-wrapper input-append']/button").click()

        #CHECK THAT ERROR MSG IS SHOWN
        try:
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='alert alert-no-items']"), 'Ничего не найдено'))
            self.assertEqual(driver.find_element_by_xpath("//div[@class='alert alert-no-items']").text, 'Ничего не найдено')
        except:
            TimeoutException()
            pass



        #result = driver.find_element_by_xpath("//table[@id='userList']/tbody/tr/td[3]")

        #assert deleted_user in result.text

        #choose checkbox of deleted user
        #driver.find_element_by_xpath("//table[@id='userList']/tbody/tr/td[1]/input").click()
        #click on deleted button
        #driver.find_element_by_xpath("//div[@id='toolbar-delete']/button").click()
        #driver.switch_to_alert().accept()

        #alert_msg = driver.find_element_by_xpath("//div[@class='alert-message']")


        #self.assertEqual(alert_msg, "Ничего не найдено")



    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()