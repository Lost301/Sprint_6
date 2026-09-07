from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def fill_first_step(self, data):
        self.type_text(OrderPageLocators.FIRST_NAME, data['first_name'])
        self.type_text(OrderPageLocators.LAST_NAME, data['last_name'])
        self.type_text(OrderPageLocators.ADDRESS, data['address'])
        self.click(OrderPageLocators.METRO)
        self.click(OrderPageLocators.metro_option(data['metro']))
        self.type_text(OrderPageLocators.PHONE, data['phone'])
        self.click(OrderPageLocators.NEXT)

    def fill_second_step(self, data):
        self.type_text(OrderPageLocators.DATE, data['date'])
        self.press_enter(OrderPageLocators.DATE)
        self.click(OrderPageLocators.RENT_PERIOD)
        self.js_click(self.find(OrderPageLocators.rent_option(data['period'])))
        self.type_text(OrderPageLocators.COMMENT, data['comment'])
        self.click(OrderPageLocators.FINAL_ORDER)
        self.js_click(self.find(OrderPageLocators.CONFIRM))

    def is_success_displayed(self):
        return self.find(OrderPageLocators.SUCCESS).is_displayed()
