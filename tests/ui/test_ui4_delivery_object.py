from modules.ui.page_objects.delivery_page import DeliveryPage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.ui1
def test_delivery():

    # creating page object (will create its own driver)
    page = DeliveryPage()

    # open the page https://www.delivery-auto.com/uk-ua/Home/Index
    page.go_to()

    # looking for the field to enter the address of the representative office and entering the address
    page.find_representative("вул. Спаська, 16")

    # checking the name of the representative office
    assert page.check_representative_name('САМАР-1 (НОВОМОСКОВСЬК-1)')

    # follow the link "Замовити забір/доставку вантажу - "НАТИСНИ ТУТ" або зателефонуй"
    page.order_pickup_delivery()

    # checking the title of the page
    assert page.check_title("Заявка на забирання/доставку вантажу | Delivery Auto")
    
    # closing the browser
    page.close()