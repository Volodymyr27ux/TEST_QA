from modules.ui.page_objects.delivery_page import DeliveryPage
import pytest

@pytest.mark.ui
def test_delivery():

    # створення об'єкту сторінки
    page = DeliveryPage()

    # відкриваємо сторінку https://www.delivery-auto.com/uk-ua/Home/Index
    page.go_to()

    #виконуємо пошук представництва 
    page.find_representative("вул. Спаська, 16")

    # перевіряємо назву знайденого представництва
    page.check_representative_name('САМАР-1 (НОВОМОСКОВСЬК-1)')

    # переходимо за посиланням "Замовити забір/доставку вантажу - "НАТИСНИ ТУТ" або зателефонуй"
    page.order_pickup_delivery()

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    page.check_title("Заявка на забирання/доставку вантажу | Delivery Auto")
    
    # Закриваємо браузер
    page.close()