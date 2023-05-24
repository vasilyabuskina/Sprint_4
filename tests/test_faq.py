import allure
from pages.faq_page import FaqPage


class TestFaq:

    def test_click_on_question_1_equal_answer_1(self, driver):
        faq = FaqPage(driver)
        faq.click_quest_1()
        faq.check_text_answer1()

    def test_click_on_question_2_equal_answer_2(self, driver):
        faq = FaqPage(driver)
        faq.click_quest_2()
        faq.check_text_answer2()

    def test_click_on_question_3_equal_answer_3(self, driver):
        faq = FaqPage(driver)
        faq.click_quest_3()
        faq.check_text_answer3()

    def test_click_on_question_4_equal_answer_4(self, driver):
        faq = FaqPage(driver)
        faq.click_quest_4()
        faq.check_text_answer4()

    def test_click_on_question_5_equal_answer_5(self, driver):
        faq = FaqPage(driver)
        faq.click_quest_5()
        faq.check_text_answer5()

    def test_click_on_question_6_equal_answer_6(self, driver):
        faq = FaqPage(driver)
        faq.click_quest_6()
        faq.check_text_answer6()

    def test_click_on_question_7_equal_answer_7(self, driver):
        faq = FaqPage(driver)
        faq.click_quest_7()
        faq.check_text_answer7()

    def test_click_on_question_8_equal_answer_8(self, driver):
        faq = FaqPage(driver)
        faq.click_quest_8()
        faq.check_text_answer8()
