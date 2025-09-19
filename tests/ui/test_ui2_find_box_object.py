from modules.ui.page_objects.find_box import FindBox
import pytest


@pytest.mark.ui1
def test_find_package():

    # creating object to manage the browser
    page = FindBox()

    # open the page https://novaposhta.ua/
    page.go_to()

    # looking for the field to enter the parcel number and entering the parcel number
    page.find_box('59001449954672')

    # checking the title of the page
    assert page.check_title("Нова пошта - доставка майбутнього")

    # checking the description of the goods sent ('Constructor')
    assert page.check_box('Конструктор')
    
    # closing the browser
    page.close()
