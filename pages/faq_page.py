import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FaqPage(BasePage):
    faq_head = [By.XPATH, '//div[text()="Вопросы о важном"]']

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    @allure.step('Сравниваем соответствие вопрос-ответ')
    def quest_match_answer(self, quest_locator, answer_locator, answer_text):
        self.wait_for_element_visibility(quest_locator).click()
        ans = self.wait_for_element_visibility(answer_locator).text
        assert ans == answer_text
