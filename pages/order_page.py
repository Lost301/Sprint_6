from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def fill_first_step(self, data):
        self.type_text(OrderPageLocators.FIRST_NAME, data['first_name'])
        self.type_text(OrderPageLocators.LAST_NAME, data['last_name'])
        self.type_text(OrderPageLocators.ADDRESS, data['address'])
        self.click(OrderPageLocators.METRO)
        metro = (By.XPATH, f"//*[contains(@class,'Order_Text') and normalize-space()='{data['metro']}']")
        self.click(metro)
        self.type_text(OrderPageLocators.PHONE, data['phone'])
        self.click(OrderPageLocators.NEXT)

    def fill_second_step(self, data):
        self.type_text(OrderPageLocators.DATE, data['date'])
        self.press_enter(OrderPageLocators.DATE)
        self.click(OrderPageLocators.RENT_PERIOD)
        self.click_visible_text(data['period'])
        self.type_text(OrderPageLocators.COMMENT, data['comment'])
        self.click(OrderPageLocators.FINAL_ORDER)
        confirm = self.wait.until(lambda driver: next(
            (button for button in driver.find_elements(*OrderPageLocators.CONFIRM) if button.is_displayed()), False))
        self.js_click(confirm)

    def is_success_displayed(self):
        return self.find(OrderPageLocators.SUCCESS).is_displayed()
