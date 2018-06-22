import pytest
import utils
from splinter import Browser
from selenium import webdriver

@pytest.yield_fixture
def test_browser(browser):
    browser.visit("http://taxi.yandex.ru")
    yield browser
    browser.quit()

class TestYandexTaxiOrder():

    def test_order_when_address_from_filled(self, test_browser):
        """Checking entering address from and than click 'demo_order' button"""
        address_from = 'Театральная площадь, 1'
        order_form = utils.TaxiOrderForm(test_browser)
        order_form.fill_from_field(address_from)
        assert order_form.find_from_field().value == address_from, "address not filled"
        demo_order_button = order_form.find_demo_order_button()
        utils.wait_until(lambda: demo_order_button.visible == True)
        demo_order_button.click()
        assert order_form.demo_progress_title().text == "Демонстрационный заказ"

    def test_order_when_address_from_and_to_filled(self, test_browser):
        """Checking entering address from and address to and than click 'demo_order' button"""
        address_from = 'Театральная площадь, 1'
        address_to = 'Красная площадь, 3'
        order_form = utils.TaxiOrderForm(test_browser)
        order_form.fill_from_field(address_from)
        assert order_form.find_from_field().value == address_from, "address from not filled"
        order_form.fill_to_field(address_to)
        assert order_form.find_to_field().value == address_to, "address to not filled"
        demo_order_button = order_form.find_demo_order_button()
        utils.wait_until(lambda: demo_order_button.visible == True)
        demo_order_button.click()
        assert order_form.demo_progress_title().text == "Демонстрационный заказ"

    def test_demo_order_button_hides_when_address_from_is_empty(self, test_browser):
        """Checking that demo order button is hidden when address from field is empty"""
        order_form = utils.TaxiOrderForm(test_browser)
        order_form.clear_from_field()
        assert not order_form.find_demo_order_button().visible, "demo order button is visible"