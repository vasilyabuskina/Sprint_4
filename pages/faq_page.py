import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class FaqPage(BasePage):
    faq_head = [By.LINK_TEXT, 'Вопросы о важном']
    question_1 = [By.ID, 'accordion__heading-0']
    question_2 = [By.ID, 'accordion__heading-1']
    question_3 = [By.ID, 'accordion__heading-2']
    question_4 = [By.ID, 'accordion__heading-3']
    question_5 = [By.ID, 'accordion__heading-4']
    question_6 = [By.ID, 'accordion__heading-5']
    question_7 = [By.ID, 'accordion__heading-6']
    question_8 = [By.ID, 'accordion__heading-7']
    answer_1 = [By.ID,'accordion__panel-0']
    answer_2 = [By.ID, 'accordion__panel-1']
    answer_3 = [By.ID, 'accordion__panel-2']
    answer_4 = [By.ID, 'accordion__panel-3']
    answer_5 = [By.ID, 'accordion__panel-4']
    answer_6 = [By.ID, 'accordion__panel-5']
    answer_7 = [By.ID, 'accordion__panel-6']
    answer_8 = [By.ID, 'accordion__panel-7']

    def __init__(self, driver):
        self.driver = driver

    def click_quest_1(self):
        self.scroll_to_element(self.question_1)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.question_1)).click()

    def click_quest_2(self):
        self.scroll_to_element(self.question_2)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.question_2)).click()

    def click_quest_3(self):
        self.scroll_to_element(self.question_3)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.question_3)).click()

    def click_quest_4(self):
        self.scroll_to_element(self.question_4)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.question_4)).click()

    def click_quest_5(self):
        self.scroll_to_element(self.question_5)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.question_5)).click()

    def click_quest_6(self):
        self.scroll_to_element(self.question_6)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.question_6)).click()

    def click_quest_7(self):
        self.scroll_to_element(self.question_7)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.question_7)).click()

    def click_quest_8(self):
        self.scroll_to_element(self.question_8)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.question_8)).click()

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        return self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))

    def check_text_answer1(self):
        answer1 = self.driver.find_element(*self.answer_1).text
        assert answer1 == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    def check_text_answer2(self):
        answer2 = self.driver.find_element(*self.answer_2).text
        assert answer2 == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    def check_text_answer3(self):
        answer3 = self.driver.find_element(*self.answer_3).text
        assert answer3 == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    def check_text_answer4(self):
        answer4 = self.driver.find_element(*self.answer_4).text
        assert answer4 == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    def check_text_answer5(self):
        answer5 = self.driver.find_element(*self.answer_5).text
        assert answer5 == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    def check_text_answer6(self):
        answer6 = self.driver.find_element(*self.answer_6).text
        assert answer6 == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    def check_text_answer7(self):
        answer7 = self.driver.find_element(*self.answer_7).text
        assert answer7 == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    def check_text_answer8(self):
        answer8 = self.driver.find_element(*self.answer_8).text
        assert answer8 == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
