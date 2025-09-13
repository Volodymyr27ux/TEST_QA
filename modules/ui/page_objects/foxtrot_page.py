from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class FoxtrotPage(BasePage):
    URL = 'https://www.foxtrot.com.ua/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(FoxtrotPage.URL)

    def search_product(self, product_name):
        # Знаходимо поле для пошуку товару і вводимо текст
        field = self.driver.find_element(By.XPATH, "//*[@id='js-fix-header']/div/div/div[4]/div[1]/input[1]")
        field.send_keys(product_name)

        # Знаходимо кнопку 'Знайти' і натискаємо її
        btn_elem = self.driver.find_element(By.XPATH, "//*[@id='js-fix-header']/div/div/div[4]/div[1]/input[2]")
        btn_elem.click()
        time.sleep(2)

    def add_product_to_cart(self):
        # Знаходимо кнопку 'купити' та емулюємо клік лівою кнопкою мишки
        buy_elem = self.driver.find_element(By.XPATH, "//*[@id='search-page-container']/div[3]/div/div/div[2]/div/div/div[2]/section/article[1]/div/div/div[3]/div[2]/div[2]/button")
        buy_elem.click()
        time.sleep(2)
        
        # Знаходимо кнопку 'перейти до кошика' та емулюємо клік лівою кнопкою мишки
        btn_elem = self.driver.find_element(By.XPATH, "//*[@id='cart-preview']/div/div[2]/div[2]/button[1]")
        btn_elem.click()
        time.sleep(2)

    def proceed_to_checkout(self):
        # Знаходимо кнопку 'оформити замовлення' та емулюємо клік лівою кнопкою мишки
        btn_elem = self.driver.find_element(By.XPATH, "//*[@id='desktop-promocode-container']/div/div[2]/div[1]")
        btn_elem.click()
        time.sleep(2)
    
    def fill_contact_details(self, city, phone, first_name, last_name, middle_name):
        # Знаходимо поле 'місто доставки' та вводимо текст
        field = self.driver.find_element(By.XPATH, "//*[@id='select2-select-city-first-container']")
        field.click()
        time.sleep(2)
        field = self.driver.find_element(By.XPATH, " //input[@type='search']")
        field.send_keys(city)
        time.sleep(3)

        # Вибираємо зі списку місто та емулюємо клік лівою кнопкою мишки 
        city_elem = self.driver.find_element(By.XPATH, "//*[@id='select2-select-city-first-results']/li[2]")
        city_elem.click()
        time.sleep(2)

        # Знаходимо поле 'ваш телефон' та вводимо номер телефону
        field = self.driver.find_element(By.XPATH, "//*[@id='Phone']")
        field.send_keys(phone)

        # Знаходимо поле 'Ім'я' та вводимо Ім'я
        field = self.driver.find_element(By.ID, "Name")
        field.send_keys(first_name)

        # Знаходимо поле 'Прізвище' та вводимо Прізвище
        field = self.driver.find_element(By.ID, "LastName")
        field.send_keys(last_name)

        # Знаходимо поле 'По батькові' та вводимо По батькові
        field = self.driver.find_element(By.ID, "MiddleName")
        field.send_keys(middle_name)
        time.sleep(2)

    def continue_checkout(self):
        # Знаходимо кнопку 'Продовжити Оформлення' для форми '1.Ваші контактні дані' та емулюємо клік лівою кнопкою мишки
        btn_elem = self.driver.find_element(By.XPATH,"//*[@id='contacts-block']/div[2]/div[2]/div[2]/div/button")
        btn_elem.click()
        time.sleep(2)
    
    def verify_contact_details(self, expected_name, expected_lastname, expected_phone):
        # Перевіряємо введені дані з форми '1.Ваші контактні дані'
        name = self.driver.find_element(By.ID, "customer-name").text
        assert name == expected_name
        lastname = self.driver.find_element(By.ID, "customer-surname").text
        assert lastname == expected_lastname
        phone = self.driver.find_element(By.ID, "customer-phone").text
        assert phone == expected_phone

    # Пробуемo закрити банер, якщо він є
    def close_banner(self):
        wait = WebDriverWait(self.driver, 4)
        try:
            banner_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[16]/div/div[2]/button[1]")))
            banner_btn.click()
        except Exception:
            pass  # Якщо банер не знайдено, продовжуємо без помилки

    def select_pickup_point(self):
        # Знаходимо елемент 'Оберіть точку самовивозу' з форми '2.Доставка' та емулюємо клік лівою кнопкою мишки
        elem = self.driver.find_element(By.ID, "select2-storeId-container")
        elem.click()
        time.sleep(2)

        # Вибираємо зі списку точку самовивозу та емулюємо клік лівою кнопкою мишки
        point_elem = self.driver.find_element(By.ID, "select2-storeId-results")
        point_elem.click()
        
    def continue_delivery(self):
        # Знаходимо кнопку 'Продовжити Оформлення' для форми '2.Доставка' та емулюємо клік лівою кнопкою мишки
        btn_elem = self.driver.find_element(By.XPATH,"//*[@id='delivery-types']/div[2]/div[2]/div[2]/button")
        btn_elem.click()
        time.sleep(2)

    # перевіряємо дані з форми '2.Доставка'
    def verify_pickup_point(self, expected_point):
        point = self.driver.find_element(By.ID, "selected-delivery-specs-title").text
        assert point == expected_point

    # форма '3.Оплата'
    def select_payment_method(self):
        # Знаходимо елемент 'Оплата при отриманні' з форми '3.Оплата'та емулюємо клік лівою кнопкою мишки
        elem = self.driver.find_element(By.XPATH, "//*[@id='payment-types']/div[2]/div[1]/div[1]/div/div[1]/div/div/label")
        elem.click()

    def continue_payment(self):
        # Знаходимо кнопку 'Продовжити Оформлення' для форми '3.Оплата' та емулюємо клік лівою кнопкою мишки
        btn_elem = self.driver.find_element(By.XPATH,"//*[@id='payment-types']/div[2]/div[2]/button")
        btn_elem.click()
        time.sleep(2)

    # перевіряємо дані з форми '3.Оплата'
    def verify_payment_method(self, expected_payment_info):
        payment_info = self.driver.find_element(By.ID, "payment-title").text 
        assert payment_info == expected_payment_info

    # форма '4.Отримувач'
    def select_recipient(self):
        # Знаходимо елемент 'Я' з форми '4.Отримувач' та емулюємо клік лівою кнопкою мишки
        elem = self.driver.find_element(By.XPATH, "//*[@id='recipient-types']/div[2]/div/div[1]/div[1]/label")
        elem.click()

        # знаходимо кнопку 'Згорнути' з форми '4.Отримувач' та емулюємо клік лівою кнопкою мишки
        btn_elem = self.driver.find_element(By.XPATH,"//*[@id='recipient-types']/div[1]/div")
        btn_elem.click()

    # перевіряємо дані з форми '4.Отримувач'
    def verify_recipient(self, expected_recipient):
        recipient = self.driver.find_element(By.XPATH, "//*[@id='checkout-form']/div[4]/div/div[6]/div[2]").text 
        assert recipient == expected_recipient
