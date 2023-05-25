import allure
import pytest
from pages.order_page import OrderPage
from datetime import datetime, timedelta

orders_data = [
    {"button": OrderPage.up_order_button,
     "firstname": 'Алиса',
     "lastname": 'Селезнева',
     "address": 'Москва, ул. Пушкинская, 15 - 12',
     "subway_station": 'Сокольники ',
     "phone": '89266379204',
     "date": (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y"),
     "duration": 5
     },
    {"button": OrderPage.down_order_button,
     "firstname": 'Александр',
     "lastname": 'Пушкин',
     "address": 'Одинцово, Сиреневая, 20',
     "subway_station": 'Лубянка ',
     "phone": '89011211212',
     "date": (datetime.now() + timedelta(days=3)).strftime("%d.%m.%Y"),
     "duration": 1
     }
]


class TestOrder:
    @allure.title('Оформление заказа')
    @pytest.mark.parametrize('order', orders_data)
    def test_place_order(self, driver, order):
        ord = OrderPage(driver)
        ord.fill_order_page(order)
