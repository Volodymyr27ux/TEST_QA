from modules.ui.page_objects.find_package import FindBox
import pytest


@pytest.mark.ui
def test_find_package():

    # створення об'єкту сторінки
    page = FindBox()

    # відкриваємо сторінку https://novaposhta.ua/
    page.go_to()

    #виконуємо пошук посилки 
    page.find_box('59001449954672')

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert page.check_title("Нова пошта - доставка майбутнього")
    
    # Закриваємо браузер
    page.close()
