import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage


@allure.feature('Навигация')
class TestNavigation:
    @allure.title('Логотип Самоката ведёт на главную страницу')
    def test_scooter_logo_opens_home(self, driver):
        page = MainPage(driver)
        page.open('https://qa-scooter.praktikum-services.ru/order')
        page.click_scooter_logo()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Логотип Яндекса открывает главную страницу Дзена')
    def test_yandex_logo_opens_dzen(self, driver):
        page = MainPage(driver)
        page.open('https://qa-scooter.praktikum-services.ru/')
        original = driver.current_window_handle
        page.click_yandex_logo()
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window([h for h in driver.window_handles if h != original][0])
        WebDriverWait(driver, 10).until(lambda d: d.current_url != 'about:blank')
        assert 'yandex.ru' in driver.current_url or 'dzen.ru' in driver.current_url
