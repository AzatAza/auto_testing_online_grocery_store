import logging
from fixture.locators.locators import Locators
from fixture.models.main_page import Product
from fixture.pages.base_page import BasePage

logger = logging.getLogger("grocery")


class MainPage(BasePage):
    def search_product(self, data: Product):
        """

        """
        logger.info(f"Search {data.product} on the grocery page")
        self.fill_element(data=data.product, locator=Locators.SEARCH_FIELD)
        self.click_element(locator=Locators.SEARCH_BUTTON)

    def add_product(self, data: Product):

        logger.info(f"Add {data.product} in the cart")
        self.fill_element(data=data.product, locator=Locators.SEARCH_FIELD)
        self.click_element(locator=Locators.SEARCH_BUTTON)
        self.click_element(locator=Locators.ADD_BUTTON)
        self.click_element(locator=Locators.BASKET_BUTTON)

    def delete_product(self):
        self.click_element(locator=Locators.DELETE_BUTTON)

    def buy_product(self):
        self.click_element(locator=Locators.BUY_BUTTON)

    def get_pay_done_text(self) -> str:
        return self.get_text(locator=Locators.PAY_DONE)

    def get_title_text(self) -> str:
        return self.get_text(locator=Locators.FOUNDED_CARD_TITTLE)

    def get_page_text(self) -> str:
        return self.get_text(locator=Locators.FOUND_NOTHING)

    def get_basket_text(self) -> str:
        return self.get_text(locator=Locators.BASKET_LIST)
