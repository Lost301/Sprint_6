import allure
from constants import BASE_URL, ORDER_URL
from pages.main_page import MainPage


@allure.feature('Навигация')
class TestNavigation:
    @allure.title('Логотип Самоката ведёт на главную страницу')
    def test_scooter_logo_opens_home(self, driver):
        page = MainPage(driver)
        page.open(ORDER_URL)
        page.click_scooter_logo()
        assert page.current_url() == BASE_URL

    @allure.title('Логотип Яндекса открывает главную страницу Дзена')
    def test_yandex_logo_opens_dzen(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL)
        original = page.current_window()
        page.click_yandex_logo()
        page.switch_to_new_window(original)
        page.wait.until(lambda d: d.current_url != 'about:blank')
        assert 'yandex.ru' in page.current_url() or 'dzen.ru' in page.current_url()
