from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def open(self, url):
        self.open_url(url)
        self.dismiss_cookie_banner()

    def scroll_to_order(self):
        self.scroll_to(MainPageLocators.ORDER_BOTTOM)

    def open_faq_item(self, index):
        self.click(MainPageLocators.FAQ_ITEMS[index])

    def faq_answer(self, index):
        locator = (MainPageLocators.FAQ_ANSWER[0], MainPageLocators.FAQ_ANSWER[1].format(index))
        return self.find(locator)

    def click_order_top(self):
        self.click(MainPageLocators.ORDER_TOP)

    def click_order_bottom(self):
        self.scroll_to_order()
        self.click(MainPageLocators.ORDER_BOTTOM)

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.open_link_in_new_tab(MainPageLocators.YANDEX_LOGO)
