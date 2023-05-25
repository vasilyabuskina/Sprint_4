import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


url = 'https://qa-scooter.praktikum-services.ru/'

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1200,800")

    browser = webdriver.Firefox(options=options)
    browser.get(url)

    yield browser
    browser.quit()