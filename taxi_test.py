import pytest
import utils
from random import randint, sample
from splinter import Browser
from selenium import webdriver

@pytest.yield_fixture
def test_browser(browser):
    browser.visit("http://taxi.yandex.ru")
    yield browser
    browser.quit()

class TestYandexTaxiOrder():

    def test_order_when_address_from_filled(self, test_browser):
        """Checking entering address from and phone number than click 'demo_order' button"""
        address_from = 'Театральная площадь, 1'
        order_form = utils.TaxiOrderForm(test_browser)
        order_form.fill_from_field(address_from)
        assert order_form.find_from_field().value == address_from, "address not filled"
        order_form.fill_phone_number_field('+79991234567')
        demo_order_button = order_form.find_demo_order_button()
        utils.wait_until(lambda: demo_order_button.visible == True)
        demo_order_button.click()
        assert order_form.demo_progress_title().text == "Демонстрационный заказ"

    def test_order_when_address_from_and_to_filled(self, test_browser):
        """Checking entering address from and address to and phone number and than click 'demo_order' button"""
        address_from = 'Театральная площадь, 1'
        address_to = 'Красная площадь, 3'
        order_form = utils.TaxiOrderForm(test_browser)
        order_form.fill_from_field(address_from)
        assert order_form.find_from_field().value == address_from, "address from not filled as expected"
        order_form.fill_to_field(address_to)
        assert order_form.find_to_field().value == address_to, "address to not filled as expected"
        order_form.fill_phone_number_field('+79991234567')
        demo_order_button = order_form.find_demo_order_button()
        utils.wait_until(lambda: demo_order_button.visible == True)
        demo_order_button.click()
        assert order_form.demo_progress_title().text == "Демонстрационный заказ"

    def test_change_to_from_swap(self, test_browser):
        """Checking swapping to and from addressess"""
        address_from = 'Театральная площадь, 1'
        address_to = 'Красная площадь, 3'
        order_form = utils.TaxiOrderForm(test_browser)
        order_form.fill_from_field(address_from)
        order_form.fill_to_field(address_to)
        order_form.find_swap_button().click()
        assert order_form.find_from_field().value == address_to, "address from not filled as expected"
        assert order_form.find_to_field().value == address_from, "address to not filled as expected"

    def test_can_cancel(self, test_browser):
        """Checking ability to cancel order"""
        address_from = 'Театральная площадь, 1'
        order_form = utils.TaxiOrderForm(test_browser)
        order_form.fill_from_field(address_from)
        assert order_form.find_from_field().value == address_from, "address not filled"
        order_form.fill_phone_number_field('+79991234567')
        demo_order_button = order_form.find_demo_order_button()
        utils.wait_until(lambda: demo_order_button.visible == True)
        demo_order_button.click()
        order_form.find_cancel_button().click()

    def test_select_some_requirements(self, test_browser):
        """Checking selecting requirements to the order"""
        number = randint(1,5)
        requirements = sample(['yellowcarnumber', 'nosmoking', 'conditioner', 'animaltransport', 'check'], number)
        order_form = utils.TaxiOrderForm(test_browser)
        order_form.select_order_requirements(requirements)
        assert order_form.find_order_requirements_button().find_by_css('i[class="requirements-count"]').text == str(number)

    def test_demo_order_button_hides_when_address_from_is_empty(self, test_browser):
        """Checking that demo order button is hidden when address from field is empty"""
        order_form = utils.TaxiOrderForm(test_browser)
        order_form.clear_from_field()
        order_form.use_location()
        assert not order_form.find_demo_order_button().visible, "demo order button is visible"