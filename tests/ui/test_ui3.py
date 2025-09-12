import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



@pytest.mark.ui
def test_amazon():
    # Створення об'єкту для керування бразуером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # відкриваємо сторінку
    driver.get("https://www.amazon.com/")
    
    # пошук потрібного елемента 'поле пошуку товарів'
    field = driver.find_element(By.ID,"twotabsearchtextbox")

    # Вводимо потрібний товар
    field.send_keys("crocs mens")

    # Знаходимо кнопку 'пошук'
    btn_elem = driver.find_element(By.XPATH, "//*[@id='nav-search-submit-button']")

    # Емулюємо клік лівою кнопкою мишки
    btn_elem.click()
    import time
    time.sleep(2)
    

    # пошуку потрібного елемента 'See options'
    btn = driver.find_element(By.ID,"a-autoid-31-announce")
    btn.click()
    import time
    time.sleep(5)
    


    # Закриваємо браузер
    driver.close()


