from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by_locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(by_locator)
        )

    def set(self, by_locator, value):
        self.find(by_locator).clear()
        self.find(by_locator).send_keys(value)

    def get_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        ).text

    def click_on(self, by_locator):
        self.find(by_locator).click()
