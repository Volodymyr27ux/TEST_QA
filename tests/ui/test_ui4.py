import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



@pytest.mark.ui
def test_delivery():
    # Створення об'єкту для керування бразуером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # відкриваємо сторінку
    driver.get("https://www.delivery-auto.com/uk-ua/Home/Index")

    # пошук потрібного елемента 'Знайти представництво'
    btn_elem = driver.find_element(By.XPATH,"//*[@id='scrollup']/main/section[2]/div/div[3]/div[1]/a[3]")

    # Емулюємо клік лівою кнопкою мишки
    btn_elem.click()
        
    # пошук потрібного поля 'Швидкий пошук представництва Delivery на карті'
    field = driver.find_element(By.ID,"representatives-search")

    # Вводимо потрібну адресу або назву представництва
    field.send_keys("вул. Спаська, 16")
    time.sleep(2)
    
    # вибір представництва зі списка у полі пошуку
    elem = driver.find_element(By.XPATH,"//*[@id='ui-id-1']/li[2]")
    elem.click()

    # пошук потрібного елемента(кнопки 'Знайти')
    btn_elem = driver.find_element(By.XPATH,"//*[@id='representatives-btn']")
    btn_elem.click()
    time.sleep(2)

    # знайдене представництвo 'САМАР-1 (НОВОМОСКОВСЬК-1)' на мапі
    elem = driver.find_element(By.XPATH,"//*[@id='header-container']")
    assert elem.text == 'САМАР-1 (НОВОМОСКОВСЬК-1)'

    # пошук потрібного посилання "Замовити забір/доставку вантажу - "НАТИСНИ ТУТ" або зателефонуй"
    # та перехід за цим посиланням
    link = driver.find_element(By.XPATH,"//*[@id='baloon-container']/div[3]/span/a")
    link.click()
    

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Заявка на забирання/доставку вантажу | Delivery Auto"

    # Закриваємо браузер
    driver.close()