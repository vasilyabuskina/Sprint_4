import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class OrderPage(BasePage):
    up_order_button = [By.XPATH, '//button[@class="Button_Button__ra12g"]']
    down_order_button = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']

    field_name = [By.XPATH, "//input[@placeholder='* Имя']"]
    field_lastname = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    field_address = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    field_subway_station = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    field_phone = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    next_button = [By.XPATH, "//button[text()='Далее']"]

    field_date = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
    field_rental_duration = [By.XPATH, ".//*[@class='Dropdown-arrow']"]
    dropdown_duration_option = {
        1: [By.XPATH, "(//div[@class='Dropdown-option'])[1]"],
        2: [By.XPATH, "(//div[@class='Dropdown-option'])[2]"],
        3: [By.XPATH, "(//div[@class='Dropdown-option'])[3]"],
        4: [By.XPATH, "(//div[@class='Dropdown-option'])[4]"],
        5: [By.XPATH, "(//div[@class='Dropdown-option'])[5]"],
        6: [By.XPATH, "(//div[@class='Dropdown-option'])[6]"],
        7: [By.XPATH, "(//div[@class='Dropdown-option'])[7]"]
    }
    order_button = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']
    order_confirmation_yes_button_on_popup_window = [By.XPATH, '//button[(text()="Да")]']
    modal_window_view_order_status_button = [By.XPATH, '//button[text()="Посмотреть статус"]']

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

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

    @allure.step('Нажимаем на верхнюю кнопку Заказать')
    def click_on_upper_order_btn(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.up_order_button)).click()

    @allure.description('Зполняем поля заказа по шагам')
    def fill_order_page(self, order):
        self.accept_cookie()
        self.driver.find_element(*(order.get('button'))).click()

        self.fill(OrderPage.field_name, order.get('firstname'))
        self.fill(OrderPage.field_lastname, order.get('lastname'))
        self.fill(OrderPage.field_address, order.get('address'))
        self.select_from_dropdown(OrderPage.field_subway_station, order.get('subway_station'))
        self.fill(OrderPage.field_phone, order.get('phone'))

        self.driver.find_element(*self.next_button).click()

        self.fill(OrderPage.field_date, order.get('date'))
        self.driver.find_element(*self.field_rental_duration).click()
        self.driver.find_element(*self.dropdown_duration_option.get(order.get('duration'))).click()

        self.driver.find_element(*self.order_button).click()

        self.driver.find_element(*self.order_confirmation_yes_button_on_popup_window).click()

        status = self.driver.find_element(*self.modal_window_view_order_status_button).text
        assert status == "Посмотреть статус"
