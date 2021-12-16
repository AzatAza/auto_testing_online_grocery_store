import logging


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from fixture.models.main_page import Product
from fixture.pages.application import Application

logger = logging.getLogger("grocery")
logger_api = logging.getLogger("api")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://berpress.github.io/online-grocery-store/",
        help="Grocery store url",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="enter 'true' if you want run tests in headless mode of browser,\n"
        "enter 'false' - if not",
    ),
    parser.addoption(
        "--product",
        action="store",
        default="bananas",
        help="enter product name",
    ),


@pytest.fixture(scope="session")
def product_data(request):
    product = request.config.getoption("--product")
    return Product(product)


@pytest.fixture()
def app(request):
    url = request.config.getoption("--url")
    # headless = request.config.getoption("--headless")

    # Driver's options
    chrome_options = Options()
    # if headless == "false":
    #     chrome_options.headless = False
    # else:
    chrome_options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    logger.info(f"Start app on {url}")
    app = Application(driver, url)
    yield app
    app.quit()
