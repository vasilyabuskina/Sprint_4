import pytest
from selenium.webdriver.common.by import By
from pages.faq_page import FaqPage
import allure


faq_data = [
    {
        "index": 0,
        "answer_text": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    },
    {
        "index": 1,
        "answer_text": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    },
    {
        "index": 2,
        "answer_text": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    },
    {
        "index": 3,
        "answer_text": "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    },
    {
        "index": 4,
        "answer_text": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    },
    {
        "index": 5,
        "answer_text": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    },
    {
        "index": 6,
        "answer_text": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    },
    {
        "index": 7,
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
        index = faq["index"]
        quest_loc = [By.ID, 'accordion__heading-'+str(index)]
        ans_loc = [By.ID, 'accordion__panel-' + str(index)]
        faq_page.quest_match_answer(quest_loc, ans_loc, faq["answer_text"])
