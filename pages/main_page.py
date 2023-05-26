import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    yandex_logo = [By.XPATH, ".//img[@alt='Yandex']"]
    scooter_logo = [By.XPATH, ".//img[@alt='Scooter']"]
    scooter_text_on_main_page = [By. XPATH, '//div[contains(text(),"Самокат")]']
    dzen_logo = [By.XPATH, '//a[@aria-label="Логотип Дзен"]']

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    @allure.step('Нажимаем на логотип Яндекса')
    def click_on_yandex_logo(self):
        self.wait_for_element_visibility(self.yandex_logo).click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Нажимаем на логотип "Самоката"')
    def click_on_scooter_logo(self):
        self.wait_for_element_visibility(self.scooter_logo).click()
