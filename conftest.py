import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



url = 'https://qa-scooter.praktikum-services.ru/'

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1200,800")

    browser = webdriver.Firefox(options=options)
    browser.get(url)

    yield browser
    browser.quit()