import allure
from pages.base_page import BasePage
from pages.order_page import OrderPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBasePage:
    @allure.title('Переход на Дзен при нажатии на логотип Яндекса')
    def test_click_on_yandex_logo_leads_to_dzen_main_page(self, driver):
        base = BasePage(driver)
        base.click_on_yandex_logo()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BasePage.dzen_logo))
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

    @allure.title('Переход на главную страницу "Самоката" при нажатии на логотип "Самоката"')
    def test_click_on_scooter_logo_leads_to_scooter_main_page(self, driver):
        base_page = BasePage(driver)
        order_page = OrderPage(driver)
        order_page.click_on_upper_order_btn()
        base_page.click_on_scooter_logo()
        text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(BasePage.scooter_text_on_main_page)).text
        assert text == "Самокат\nна пару дней\nПривезём его прямо к вашей двери,\nа когда накатаетесь — заберём"


