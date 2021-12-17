import pytest
from fixture.constans import Constans


class TestMainPage:
    def test_search_input_with_valid_data(self, app, product_data):
        """
        Steps:
        1. Open main page
        2. Add existing product in search input
        3. Check result
        """
        app.open_main_page()
        app.search.search_product(data=product_data)
        assert app.search.get_title_text() == product_data.product
    
    @pytest.mark.xfail(reason="feature is not ready")
    def test_search_input_with_invalid_data(self, app, product_data):
        """
        Steps:
        1. Open main page
        2. Add some word in search input
        3. Check result
        """
        app.open_main_page()
        product_data = product_data.random()
        app.search.search_product(data=product_data)
        assert app.search.get_page_text() == Constans.FOUND_NOTHING

    def test_add_product_in_basket(self, app, product_data):
        """
        Steps:
        1. Open main page
        2. Add product in the basket
        3. Check result
        """
        app.open_main_page()
        app.search.add_product(data=product_data)
        assert product_data.product in app.search.get_basket_text()

    def test_delete_product_from_basket(self, app, product_data):
        """
        Steps:
        1. Open main page
        2. Add existing product in search input
        3. Delete added product from basket
        3. Check result
        """
        app.open_main_page()
        app.search.add_product(data=product_data)
        app.search.delete_product()
        assert Constans.EMPTY_CART in app.search.get_basket_text()

    def test_buy_product_from_basket(self, app, product_data):
        """
        Steps:
        1. Open main page
        2. Add existing product in search input
        3. Buy added product
        3. Check result
        """
        app.open_main_page()
        app.search.add_product(data=product_data)
        app.search.buy_product()
        assert Constans.PAY_DONE in app.search.get_pay_done_text()
