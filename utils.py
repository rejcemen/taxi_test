import time
from splinter import Browser
from selenium import webdriver

def wait_until(condition, interval=0.1, timeout=1, *args):
    start = time.time()
    while not condition(*args) and time.time() - start < timeout:
        time.sleep(interval)

class TaxiOrderForm:

    def __init__(self, browser):
        self.browser = browser

    def select_list_item_in_popup(self, index):
        self.browser.find_by_css('div[class*="popup_visibility_visible"]').find_by_css('li[class*="b-autocomplete-item_type_taxi"]')[index].click()

    def clear_from_field(self):
        self.browser.find_by_css('span[class="input__clear input__clear_visibility_visible"]').click()

    def use_location(self):
        self.browser.find_by_css('span[class="input__location"]').click()

    def find_swap_button(self):
        return self.browser.find_by_css('button[class="geo-group__swap js-swap-address"]')

    def fill_from_field(self, fromAddress):
        self.browser.fill('gfrom', fromAddress)
        self.select_list_item_in_popup(0)

    def find_from_field(self):
        return self.browser.find_by_name('gfrom')

    def fill_to_field(self, toAddress):
        self.browser.fill('gto', toAddress)
        self.select_list_item_in_popup(0)

    def find_to_field(self):
        return self.browser.find_by_name('gto')

    def fill_phone_number_field(self, phone_number):
        self.browser.fill('phone', phone_number)

    def find_order_requirements_button(self):
        return self.browser.find_by_css('button[class*="button_preset_requirements"]')

    def select_order_requirements(self, requirements):
        self.find_order_requirements_button().click()
        for req_id in requirements:
            self.browser.find_by_id(req_id).check()

    def find_demo_order_button(self):
        return self.browser.find_by_css('button[class*="button_action_demo"]')

    def demo_progress_title(self):
        return self.browser.find_by_css('div[class="demo-progress__title"]')

    def find_cancel_button(self):
        return self.browser.find_by_css('button[class*="js-orderBreak"]')