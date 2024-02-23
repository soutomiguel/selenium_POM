from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.test_data import TestData


class SigninPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.URL)

        self.signin_register_button = (By.CSS_SELECTOR, ".default-link.-md.link.text-uppercase[href='#']")
        self.close_popup_button = (By.XPATH, "//*[name()='circle' and contains(@cx,'10')]")
        self.email_field = (By.XPATH, "//form[@id='new_user']//input[@id='user_email']")
        self.password_field = (By.XPATH, "//form[@id='new_user']//input[@id='user_password']")
        self.login_button = (By.XPATH, "//input[@value='sign in']")
        self.login_success_message = (By.XPATH, "//div[@class='toast-message']")

        global base_page
        base_page = BasePage(self.driver)

    def close_popup(self):
        base_page.click_on(self.close_popup_button)

    def click_signin_register_button(self):
        base_page.click_on(self.signin_register_button)

    def set_email_address(self, email_address):
        base_page.set(self.email_field, email_address)

    def set_passwd(self, password):
        base_page.set(self.password_field, password)

    def click_on_login(self):
        base_page.click_on(self.login_button)

    def get_login_success_text(self):
        return base_page.get_text(self.login_success_message)
