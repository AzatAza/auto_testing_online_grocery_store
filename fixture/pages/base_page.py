import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, app):
        self.app = app

    def find_element(self, locator, wait_time=10) -> WebElement:
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Cant{locator}",
        )
        return element

    def click_element(self, locator):
        """
        Click_element == click()
        """
        element = self.find_element(locator)
        element.click()
        time.sleep(3)

    def fill_element(self, data, locator, wait_time=10):
        """
        Fill element == send_keys()
        """
        element = self.find_element(locator, wait_time)
        if data:
            element.clear()
            element.send_keys(data)

    def get_text(self, locator, wait_time=10) -> str:
        """
        Get element text
        """
        element = self.find_element(locator, wait_time)
        return element.text
