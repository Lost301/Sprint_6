import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


DATA = [
    {'first_name': 'Иван', 'last_name': 'Иванов', 'address': 'Тверская, 1', 'metro': 'Черкизовская', 'phone': '+79990000001', 'date': '10.09.2026', 'period': 'сутки', 'comment': 'Позвонить заранее'},
    {'first_name': 'Анна', 'last_name': 'Петрова', 'address': 'Ленина, 10', 'metro': 'Сокольники', 'phone': '+79990000002', 'date': '11.09.2026', 'period': 'двое суток', 'comment': 'Оставить у двери'},
]


@allure.feature('Заказ самоката')
class TestOrder:
    @pytest.mark.parametrize('data', DATA)
    @pytest.mark.parametrize('entry', ['top', 'bottom'])
    @allure.title('Позитивный заказ через кнопку {entry}')
    @allure.description('Заполняем форму заказа и проверяем сообщение об успешном создании заказа.')
    def test_order_is_created(self, driver, data, entry):
        main = MainPage(driver)
        main.open('https://qa-scooter.praktikum-services.ru/')
        if entry == 'top':
            main.click_order_top()
        else:
            main.click_order_bottom()
        order = OrderPage(driver)
        order.fill_first_step(data)
        order.fill_second_step(data)
        assert order.is_success_displayed()

