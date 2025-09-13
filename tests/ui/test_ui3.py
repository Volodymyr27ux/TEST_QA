
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



@pytest.mark.ui
def test_amazon():
    # Створення об'єкту для керування бразуером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # відкриваємо сторінку
    driver.get("https://www.amazon.com/")
    driver.maximize_window()
    
    # пошук потрібного елемента 'поле пошуку товарів'
    field = driver.find_element(By.ID,"twotabsearchtextbox")

    # Вводимо потрібний товар
    field.send_keys("crocs mens")

    # Знаходимо кнопку 'пошук'
    btn_elem = driver.find_element(By.XPATH, "//*[@id='nav-search-submit-button']")

    # Емулюємо клік лівою кнопкою мишки
    btn_elem.click()
    time.sleep(2)
    

    # пошуку потрібного елемента 'See options'
    btn = driver.find_element(By.ID,"a-autoid-31-announce")
    btn.click()
    
    # Закриваємо браузер
    driver.close()
