import pytest
from selenium import webdriver


BASE_URL = 'https://qa-scooter.praktikum-services.ru/'


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()

