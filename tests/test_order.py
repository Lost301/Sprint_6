import allure
import pytest
from constants import BASE_URL
from test_data import ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature('Заказ самоката')
class TestOrder:
    @pytest.mark.parametrize('data', ORDER_DATA)
    @allure.title('Позитивный заказ через верхнюю кнопку')
    def test_order_from_top_button(self, driver, data):
        main = MainPage(driver)
        main.open(BASE_URL)
        main.click_order_top()
        self._complete_order(driver, data)

    @pytest.mark.parametrize('data', ORDER_DATA)
    @allure.title('Позитивный заказ через нижнюю кнопку')
    def test_order_from_bottom_button(self, driver, data):
        main = MainPage(driver)
        main.open(BASE_URL)
        main.click_order_bottom()
        self._complete_order(driver, data)

    @staticmethod
    def _complete_order(driver, data):
        order = OrderPage(driver)
        order.fill_first_step(data)
        order.fill_second_step(data)
        assert order.is_success_displayed()

