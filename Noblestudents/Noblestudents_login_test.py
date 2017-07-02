import unittest
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class RegisterStudentCheckAlert(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:\Pycharm\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        #parametrs
        self.email = 'child.second@mail.ru'
        self.password = 'qwerty1A.'

        self.driver.get("https://stage.noblestudents.ready4.today")

    def test_register_and_check_alerts(self):
        driver = self.driver

        email = self.email
        password = self.password
        #click on Register-for-free button
        driver.find_element_by_xpath("//span/descendant::li[2]/a").click()
        driver.switch_to.window(driver.window_handles[0])

        #filling the registration form
        driver.find_element_by_id("jform_name").send_keys("autotest_username_1")
        #WebDriverWait(driver, 10).until(EC.)
        if driver.find_element_by_id("jform_name").get_attribute('data-validation-error') is not None:
            WebDriverWait(driver, 5)
        else:
            print("jform_name")
        driver.find_element_by_id("jform_profile_default_lastname").send_keys("autotest_username")
        if driver.find_element_by_id("jform_profile_default_lastname").get_attribute('data-validation-error'):
            WebDriverWait(driver, 5)
        else:
            print("jform_profile_default_lastname")
        driver.find_element_by_id("jform_email1").send_keys(email)
        if driver.find_element_by_id("jform_email1").get_attribute('data-validation-error') is not None:
            WebDriverWait(driver, 5)
        else:
            print("jform_email1")
        driver.find_element_by_id("jform_email2").send_keys(email)
        if driver.find_element_by_id("jform_email2").get_attribute('data-validation-error') is not None:
            WebDriverWait(driver, 5)
        else:
            print("jform_email2")
        driver.find_element_by_id("jform_password1").send_keys(password)
        if driver.find_element_by_id("jform_password1").get_attribute('data-validation-error') is not None:
            WebDriverWait(driver, 5)
        else:
            print("jform_password1")
        driver.find_element_by_link_text('Student').click()

        button = driver.find_element_by_xpath("//button[parent::div[@class='controls']]")

        self.assertTrue(button.is_displayed() and button.is_enabled())
        driver.implicitly_wait(button.is_enabled())

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[parent::div[@class='controls']]")))
        button.click()


        msg = 'Your account has been created and an activation link has been sent to the email address you entered. Note that you must activate the account by selecting the activation link when you get the email before you can login.'
        WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='alert-message'][1]"), msg))
        self.assertEqual(driver.find_element_by_xpath("//div[@class='alert-message'][1]").text, msg)


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()