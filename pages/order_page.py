from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT = (By.XPATH, "//button[normalize-space()='Далее']")
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    RENT_PERIOD = (By.CSS_SELECTOR, "div.Dropdown-root div.Dropdown-control")
    FINAL_ORDER = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[normalize-space()='Заказать']")
    CONFIRM = (By.CSS_SELECTOR, "div[class*='Order_Modal'] div[class*='Order_Buttons'] button:nth-child(2)")
    SUCCESS = (By.XPATH, "//*[contains(text(),'Заказ оформлен')]")

    def fill_first_step(self, data):
        self.type_text(self.FIRST_NAME, data['first_name'])
        self.type_text(self.LAST_NAME, data['last_name'])
        self.type_text(self.ADDRESS, data['address'])
        self.click(self.METRO)
        self.find((By.XPATH, f"//*[contains(@class,'Order_Text') and normalize-space()='{data['metro']}']")).click()
        self.type_text(self.PHONE, data['phone'])
        self.click(self.NEXT)

    def fill_second_step(self, data):
        self.type_text(self.DATE, data['date'])
        self.driver.find_element(*self.DATE).send_keys('\ue007')
        self.click(self.RENT_PERIOD)
        option = self.wait.until(lambda driver: next(
            (element for element in driver.find_elements(By.XPATH, "//*[normalize-space()=" + repr(data['period']) + "]") if element.is_displayed()),
            False,
        ))
        self.driver.execute_script("arguments[0].click();", option)
        self.type_text(self.COMMENT, data['comment'])
        self.click(self.FINAL_ORDER)
        confirm = self.wait.until(lambda driver: next(
            (button for button in driver.find_elements(*self.CONFIRM) if button.is_displayed()),
            False,
        ))
        self.driver.execute_script("arguments[0].click();", confirm)

    def is_success_displayed(self):
        return self.find(self.SUCCESS).is_displayed()
