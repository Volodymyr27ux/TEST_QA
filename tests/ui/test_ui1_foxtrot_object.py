from modules.ui.page_objects.foxtrot_page import FoxtrotPage
import pytest


@pytest.mark.ui1
def test_foxtrot():
    # Testing foxtrot.com.ua website - product search, adding to cart, order checkout
    
    # Create browser management object
    page = FoxtrotPage()

    # open the page
    page.go_to()
    page.driver.maximize_window()
    
    # find product
    page.search_product("телевізор xiaomi")

    # add product to cart
    page.add_product_to_cart()

    # ordering
    page.proceed_to_checkout()

    # filling in contact data
    page.fill_contact_details("Самар", "0631234567", "Володимир", "Черненко", "Васильович")

    # We check the data entered from the form'1.Ваші контактні дані'
    page.continue_checkout()
    page.assert_contact_details("Володимир", "Черненко", "+38(063) 1234567")

    # Try to close the banner if it is
    page.close_banner()

    # form '2.Доставка'
    page.select_pickup_point()
    page.continue_delivery()

    # We check the data from the form '2.Доставка'
    page.assert_pickup_point("МАГ ДН Самар, Гетьманська вул., 47А")

    # form '3.Оплата'
    page.select_payment_method()
    page.continue_payment()

    # We check the data from the form'3.Оплата'
    page.assert_payment_method("Оплата при отриманні")

    # form '4.Отримувач'
    page.select_recipient()
    
    # We check the data from the form '4.Отримувач'
    page.assert_recipient("Володимир Черненко   +38 (063) 123 45 67")

    page.close()
