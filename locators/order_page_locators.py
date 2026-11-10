from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT = (By.XPATH, "//button[normalize-space()='Далее']")
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD = (By.CSS_SELECTOR, 'div.Dropdown-root div.Dropdown-control')
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    FINAL_ORDER = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[normalize-space()='Заказать']")
    CONFIRM = (By.CSS_SELECTOR, "div[class*='Order_Modal'] div[class*='Order_Buttons'] button:nth-child(2)")
    SUCCESS = (By.XPATH, "//*[contains(text(),'Заказ оформлен')]")

    @staticmethod
    def metro_option(metro):
        return By.XPATH, f"//*[contains(@class,'Order_Text') and normalize-space()='{metro}']"

    @staticmethod
    def rent_option(period):
        return By.XPATH, f"//*[normalize-space()={period!r}]"
