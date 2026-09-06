from selenium.webdriver.common.by import By


class MainPageLocators:
    FAQ_ITEMS = [(By.ID, f'accordion__heading-{index}') for index in range(8)]
    FAQ_ANSWER = (By.ID, 'accordion__panel-{}')
    ORDER_TOP = (By.XPATH, "(//button[normalize-space()='Заказать'])[1]")
    ORDER_BOTTOM = (By.XPATH, "(//button[normalize-space()='Заказать'])[last()]")
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CSS_SELECTOR, 'a.Header_LogoYandex__3TSOI')

