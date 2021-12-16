from selenium.webdriver.common.by import By


class Locators:
    SEARCH_FIELD = (By.ID, "email_inline")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.search-btn")
    FOUNDED_CARD_TITTLE = (By.CLASS_NAME, "card-title")
    ADD_BUTTON = (By.XPATH, "//button[text()='Buy']")
    FOUND_NOTHING = (By.CSS_SELECTOR, 'h3')
    BASKET_BUTTON = (By.CSS_SELECTOR, "div.cart.red.darken-4.white-text")
    BASKET_LIST = (By.CSS_SELECTOR, "ui.collection.basket-list")
    DELETE_BUTTON = (By.CSS_SELECTOR, "i.material-icons.basket-delete")
    BUY_BUTTON = (By.CSS_SELECTOR, "button.btn.red.btn-small")
    PAY_DONE = (By.CLASS_NAME, "toast")