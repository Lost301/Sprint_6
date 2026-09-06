import allure
import pytest
from pages.main_page import MainPage


@allure.feature('FAQ')
class TestFAQ:
    @pytest.mark.parametrize('index', range(8))
    @allure.title('Открывается ответ на вопрос FAQ №{index}')
    @allure.description('Проверяем, что при клике на стрелку открывается соответствующий текст.')
    @allure.step('Открываем вопрос FAQ №{index}')
    def test_faq_answer_is_opened(self, driver, index):
        page = MainPage(driver)
        page.open('https://qa-scooter.praktikum-services.ru/')
        page.open_faq_item(index)
        assert page.faq_answer(index).is_displayed()
