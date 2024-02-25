from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.test_data import TestData


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.URL)

        global base_page
        base_page = BasePage(self.driver)

        self.signin_register_button = (By.XPATH, "(//a[@href='#'][contains(.,'Sign In/Register')])[1]")
        self.register_button = (By.XPATH, "(//a[@href='#'][contains(.,'Register')])[3]")

    def go_to_register_section(self):
        base_page.click_on(self.signin_register_button)
