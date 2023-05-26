import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Принимаем куки')
    def accept_cookie(self):
        cookie_button = [By.ID, 'rcc-confirm-button']
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(cookie_button)).click()

    @allure.step('Заполняем поле значением: {value}')
    def fill(self, locator, value):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).send_keys(value)

    @allure.step('Выбираем значение {value} из выпадающего списка')
    def select_from_dropdown(self, locator, value):
        # click on dropdown
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).send_keys(value)
        # click on option
        loc = [By.CLASS_NAME, 'select-search__select']
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc)).click()

    def wait_for_element_visibility(self, locator):
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return el

