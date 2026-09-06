from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    FAQ_ITEMS = [
        (By.ID, 'accordion__heading-0'), (By.ID, 'accordion__heading-1'),
        (By.ID, 'accordion__heading-2'), (By.ID, 'accordion__heading-3'),
        (By.ID, 'accordion__heading-4'), (By.ID, 'accordion__heading-5'),
        (By.ID, 'accordion__heading-6'), (By.ID, 'accordion__heading-7'),
    ]
    ORDER_TOP = (By.XPATH, "(//button[normalize-space()='Заказать'])[1]")
    ORDER_BOTTOM = (By.XPATH, "(//button[normalize-space()='Заказать'])[last()]")
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")

    def open(self, url):
        self.driver.get(url)
        self.dismiss_cookie_banner()

    def scroll_to_order(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find(self.ORDER_BOTTOM))

    def open_faq_item(self, index):
        self.click(self.FAQ_ITEMS[index])

    def faq_answer(self, index):
        return self.find((By.ID, f'accordion__panel-{index}'))

    def click_order_top(self):
        self.click(self.ORDER_TOP)

    def click_order_bottom(self):
        self.scroll_to_order()
        self.click(self.ORDER_BOTTOM)

    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        logo = self.find(self.YANDEX_LOGO)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", logo)
        self.driver.execute_script("arguments[0].click();", logo)
