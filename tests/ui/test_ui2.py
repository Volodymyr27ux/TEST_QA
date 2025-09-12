import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



@pytest.mark.ui
def test_posilka():
    # Створення об'єкту для керування бразуером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # відкриваємо сторінку https://github.com/login 
    driver.get("https://novaposhta.ua/")

    # Знаходимо поле, в яке будемо вводити номер посилки
    field = driver.find_element(By.XPATH, "//input[@placeholder='Введіть номер посилки']")

    # Вводимо номер посилки
    field.send_keys("59001449954672")

    # Знаходимо кнопку 'Відстежити'
    btn_elem = driver.find_element(By.XPATH, "//*[@id='__nuxt']/div/main/div/section/div/div[3]/div/div[2]/button")

    # Емулюємо клік лівою кнопкою мишки
    btn_elem.click()
    import time
    time.sleep(3)
    
    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Відстежити посилку"

    # Знаходимо в описі товар який відправлено('Конструктор')
    elem = driver.find_element(By.XPATH,"//*[@id='__nuxt']/div/main/div/div[3]/div/div/div/div[1]/div[3]/div[2]/div/ul/li[5]/div[2]/p")
    value_elem = elem.text
    assert value_elem == 'Конструктор'
    

    # Закриваємо браузер
    driver.close()