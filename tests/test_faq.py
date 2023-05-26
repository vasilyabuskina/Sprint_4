import pytest
from selenium.webdriver.common.by import By
from pages.faq_page import FaqPage
import allure


faq_data = [
    {
        "question": [By.ID, 'accordion__heading-0'],
        "answer": [By.ID, 'accordion__panel-0'],
        "answer_text": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    },
    {
        "question": [By.ID, 'accordion__heading-1'],
        "answer": [By.ID, 'accordion__panel-1'],
        "answer_text": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    },
    {
        "question": [By.ID, 'accordion__heading-2'],
        "answer": [By.ID, 'accordion__panel-2'],
        "answer_text": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    },
    {
        "question": [By.ID, 'accordion__heading-3'],
        "answer": [By.ID, 'accordion__panel-3'],
        "answer_text": "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    },
    {
        "question": [By.ID, 'accordion__heading-4'],
        "answer": [By.ID, 'accordion__panel-4'],
        "answer_text": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    },
    {
        "question": [By.ID, 'accordion__heading-5'],
        "answer": [By.ID, 'accordion__panel-5'],
        "answer_text": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    },
    {
        "question": [By.ID, 'accordion__heading-6'],
        "answer": [By.ID, 'accordion__panel-6'],
        "answer_text": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    },
    {
        "question": [By.ID, 'accordion__heading-7'],
        "answer": [By.ID, 'accordion__panel-7'],
        "answer_text": "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    },
]


@allure.title('Проверка вопросов о важном')
class TestFaq:

    @pytest.mark.parametrize('faq', faq_data)
    def test_quest_matches_answer(self, driver, faq):
        faq_page = FaqPage(driver)
        faq_page.accept_cookie()
        faq_page.scroll_to_element(faq_page.faq_head)
        faq_page.quest_match_answer(faq["question"], faq["answer"], faq["answer_text"])
