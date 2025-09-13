from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class DeliveryPage(BasePage):
    URL = 'https://www.delivery-auto.com/uk-ua/Home/Index'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(DeliveryPage.URL)

    def find_representative(self, address):
        # пошук потрібного елемента 'Знайти представництво'
        btn_elem = self.driver.find_element(By.XPATH,"//*[@id='scrollup']/main/section[2]/div/div[3]/div[1]/a[3]")

        # Емулюємо клік лівою кнопкою мишки
        btn_elem.click()
        
        # пошук потрібного поля 'Швидкий пошук представництва Delivery на карті'
        field = self.driver.find_element(By.ID,"representatives-search")

        # Вводимо потрібну адресу або назву представництва
        field.send_keys(address)
        time.sleep(2)
        
        # вибір представництва зі списка у полі пошуку
        elem = self.driver.find_element(By.XPATH,"//*[@id='ui-id-1']/li[2]")
        elem.click()

        # пошук потрібного елемента(кнопки 'Знайти')
        btn_elem = self.driver.find_element(By.XPATH,"//*[@id='representatives-btn']")
        btn_elem.click()
        time.sleep(2)

    def check_representative_name(self, expected_name):
        # знайдене представництвo 'САМАР-1 (НОВОМОСКОВСЬК-1)' на мапі
        elem = self.driver.find_element(By.XPATH,"//*[@id='header-container']")
        assert elem.text == expected_name

    def order_pickup_delivery(self):
        # пошук потрібного посилання "Замовити забір/доставку вантажу - "НАТИСНИ ТУТ" або зателефонуй"
        # та перехід за цим посиланням
        link = self.driver.find_element(By.XPATH,"//*[@id='baloon-container']/div[3]/span/a")
        link.click()
    
    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    def check_title(self, expected_title):
        assert self.driver.title == expected_title