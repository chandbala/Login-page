from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import unittest
from GuviProject.POMProjectDemo.Pages.LoginPage import LoginPage
from GuviProject.POMProjectDemo.Pages.HomePage import HomePage

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        time.sleep(10)

    def test_02_login_invalid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

            login = LoginPage(driver)
            login.enter_username("Admin")
            login.enter_password("Invalid password")
            login.click_login()
            login.check_invalidlogin()
            time.sleep(10)

    @classmethod
    def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")