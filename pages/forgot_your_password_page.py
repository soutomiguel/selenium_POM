from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.test_data import TestData


class ForgotYourPassword:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.URL)

        global base_page
        base_page = BasePage(self.driver)

        self.forgot_your_password_button = (By.XPATH, "(//a[@href='#'][contains(.,'forgot your password?')])[1]")

    def click_on_forgot_your_password_button(self):
        base_page.click_on(self.forgot_your_password_button)

