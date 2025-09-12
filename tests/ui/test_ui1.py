import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.mark.ui
def test_foxtrot():
    #Тестування сайту foxtrot.com.ua - пошук товару, додавання до кошика, оформлення замовлення
    
    # Створення об'єкту для керування бразуером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # відкриваємо сторінку
    driver.get("https://www.foxtrot.com.ua/")
    driver.maximize_window()
    
    # знаходимо поле для пошуку товару і вводимо текст
    field = driver.find_element(By.XPATH, "//*[@id='js-fix-header']/div/div/div[4]/div[1]/input[1]")
    field.send_keys("телевізор xiaomi")

    # знаходимо кнопку 'Знайти' і натискаємо її
    btn_elem = driver.find_element(By.XPATH, "//*[@id='js-fix-header']/div/div/div[4]/div[1]/input[2]")
    btn_elem.click()

    # Знаходимо кнопку 'купити' та емулюємо клік лівою кнопкою мишки
    buy_elem = driver.find_element(By.XPATH, "//*[@id='search-page-container']/div[3]/div/div/div[2]/div/div/div[2]/section/article[1]/div/div/div[3]/div[2]/div[2]/button")
    buy_elem.click()
    time.sleep(2)

    # знаходимо кнопку 'перейти до кошика' та емулюємо клік лівою кнопкою мишки
    btn_elem = driver.find_element(By.XPATH, "//*[@id='cart-preview']/div/div[2]/div[2]/button[1]")
    btn_elem.click()

    # знаходимо кнопку 'оформити замовлення' та емулюємо клік лівою кнопкою мишки
    btn_elem = driver.find_element(By.XPATH, "//*[@id='desktop-promocode-container']/div/div[2]/div[1]")
    btn_elem.click()

    # знаходимо поле 'місто доставки' та вводимо текст
    field = driver.find_element(By.XPATH, "//*[@id='select2-select-city-first-container']")
    field.click()
    time.sleep(2)
    field = driver.find_element(By.XPATH, " //input[@type='search']")
    field.send_keys("Самар")
    time.sleep(3)

    # вибираємо зі списку місто 'Самар, Дніпропетровська обл.' та емулюємо клік лівою кнопкою мишки 
    city_elem = driver.find_element(By.XPATH, "//*[@id='select2-select-city-first-results']/li[2]")
    city_elem.click()

    # знаходимо поле 'ваш телефон' та вводимо номер телефону
    field = driver.find_element(By.XPATH, "//*[@id='Phone']")
    field.send_keys("0637192271")

    # знаходимо поле 'Ім'я' та вводимо Ім'я
    field = driver.find_element(By.ID, "Name")
    field.send_keys("Володимир")

    # знаходимо поле 'Прізвище' та вводимо Прізвище
    field = driver.find_element(By.ID, "LastName")
    field.send_keys("Черненко")

    # знаходимо поле 'По батькові' та вводимо По батькові
    field = driver.find_element(By.ID, "MiddleName")
    field.send_keys("Васильович")

    # знаходимо кнопку 'Продовжити Оформлення' для форми '1.Ваші контактні дані' та емулюємо клік лівою кнопкою мишки
    btn_elem = driver.find_element(By.XPATH,"//*[@id='contacts-block']/div[2]/div[2]/div[2]/div/button")
    btn_elem.click()
    time.sleep(2)

    # перевіряємо введені дані з форми '1.Ваші контактні дані'
    name = driver.find_element(By.ID, "customer-name").text
    assert name == "Володимир"
    lastname = driver.find_element(By.ID, "customer-surname").text
    assert lastname == "Черненко"
    phone = driver.find_element(By.ID, "customer-phone").text
    assert phone == "+38(063) 7192271"

    # Пробуемo закрити банер, якщо він є
    wait = WebDriverWait(driver, 4)
    try:
        cookie_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[16]/div/div[2]/button[1]"))
        )
        cookie_btn.click()
    except Exception:
        pass  # Якщо банер не знайдено, продовжуємо без помилки
   
    # знаходимо елемент 'Оберіть точку самовивозу' з форми '2.Доставка' та емулюємо клік лівою кнопкою мишки
    elem = driver.find_element(By.ID, "select2-storeId-container")
    elem.click()
    time.sleep(2)

    # вибираємо зі списку точку самовивозу 'МАГ ДН Самар, Гетьманська вул., 47А' та емулюємо клік лівою кнопкою мишки
    point_elem = driver.find_element(By.ID, "select2-storeId-results")
    point_elem.click()
    
    # знаходимо кнопку 'Продовжити Оформлення' для форми '2.Доставка' та емулюємо клік лівою кнопкою мишки
    btn_elem = driver.find_element(By.XPATH,"//*[@id='delivery-types']/div[2]/div[2]/div[2]/button")
    btn_elem.click()
    time.sleep(2)
    
    # перевіряємо дані з форми '2.Доставка'
    shop_delivery = driver.find_element(By.ID, "selected-delivery-specs-title").text
    assert shop_delivery == "МАГ ДН Самар, Гетьманська вул., 47А"

    # Знаходимо елемент 'Оплата при отриманні' з форми '3.Оплата'та емулюємо клік лівою кнопкою мишки
    elem = driver.find_element(By.XPATH, "//*[@id='payment-types']/div[2]/div[1]/div[1]/div/div[1]/div/div/label")
    elem.click()    

    # знаходимо кнопку 'Продовжити Оформлення' для форми '3.Оплата' та емулюємо клік лівою кнопкою мишки
    btn_elem = driver.find_element(By.XPATH,"//*[@id='payment-types']/div[2]/div[2]/button")
    btn_elem.click()
    time.sleep(2)

    # перевіряємо дані з форми '3.Оплата'
    payment_info = driver.find_element(By.ID, "payment-title").text 
    assert payment_info == "Оплата при отриманні"

    # Знаходимо елемент 'Я' з форми '4.Отримувач' та емулюємо клік лівою кнопкою мишки
    elem = driver.find_element(By.XPATH, "//*[@id='recipient-types']/div[2]/div/div[1]/div[1]/label")
    elem.click()
    
    # знаходимо кнопку 'Згорнути' з форми '4.Отримувач' та емулюємо клік лівою кнопкою мишки
    btn_elem = driver.find_element(By.XPATH,"//*[@id='recipient-types']/div[1]/div")
    btn_elem.click()
    

    # перевіряємо дані з форми '4.Отримувач'
    recipient_info = driver.find_element(By.XPATH, "//*[@id='checkout-form']/div[4]/div/div[6]/div[2]").text
    assert recipient_info == "Володимир Черненко   +38 (063) 719 22 71"

    

    
    driver.quit()


