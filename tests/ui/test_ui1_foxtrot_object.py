from modules.ui.page_objects.foxtrot_page import FoxtrotPage
import pytest
import time


@pytest.mark.ui1
def test_foxtrot():
    #Тестування сайту foxtrot.com.ua - пошук товару, додавання до кошика, оформлення замовлення
    
    # Створення об'єкту для керування бразуером
    page = FoxtrotPage()

    # відкриваємо сторінку
    page.go_to()
    page.driver.maximize_window()
    
    # пошук товару
    page.search_product("телевізор xiaomi")

    # додавання товару до кошика
    page.add_product_to_cart()

    # оформлення замовлення
    page.proceed_to_checkout()

    # заповнення контактних даних
    page.fill_contact_details("Самар", "0631234567", "Володимир", "Черненко", "Васильович")

    # Перевіряємо введені дані з форми '1.Ваші контактні дані'
    page.continue_checkout()
    page.assert_contact_details("Володимир", "Черненко", "+38(063) 1234567")

    # Пробуемo закрити банер, якщо він є
    page.close_banner()

    # форма '2.Доставка'
    page.select_pickup_point()
    page.continue_delivery()

    # перевіряємо дані з форми '2.Доставка'
    page.assert_pickup_point("МАГ ДН Самар, Гетьманська вул., 47А")

    # форма '3.Оплата'
    page.select_payment_method()
    page.continue_payment()

    # перевіряємо дані з форми '3.Оплата'
    page.assert_payment_method("Оплата при отриманні")

    # форма '4.Отримувач'
    page.select_recipient()
    
    # перевіряємо дані з форми '4.Отримувач'
    page.assert_recipient("Володимир Черненко   +38 (063) 123 45 67")

    # Закриваємо браузер
    page.close()
