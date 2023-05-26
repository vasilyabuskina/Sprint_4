import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestMainPage:
    @allure.title('Переход на Дзен при нажатии на логотип Яндекса')
    def test_click_on_yandex_logo_leads_to_dzen_main_page(self, driver):
        main = MainPage(driver)
        main.click_on_yandex_logo()
        main.wait_for_element_visibility(main.dzen_logo)
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

    @allure.title('Переход на главную страницу "Самоката" при нажатии на логотип "Самоката"')
    def test_click_on_scooter_logo_leads_to_scooter_main_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_page.click_on_upper_order_btn()
        main_page.click_on_scooter_logo()
        text = main_page.wait_for_element_visibility(main_page.scooter_text_on_main_page).text
        assert text == "Самокат\nна пару дней\nПривезём его прямо к вашей двери,\nа когда накатаетесь — заберём"


