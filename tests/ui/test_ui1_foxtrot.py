import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.mark.ui
def test_foxtrot(): #Testing the site foxtrot.com.ua -searching for goods, adding to your cart, ordering an order
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://www.foxtrot.com.ua/")
    driver.maximize_window()
    
    field = driver.find_element(By.XPATH, "//*[@id='js-fix-header']/div/div/div[4]/div[1]/input[1]")
    field.send_keys("телевізор xiaomi")

    btn_elem = driver.find_element(By.XPATH, "//*[@id='js-fix-header']/div/div/div[4]/div[1]/input[2]")
    btn_elem.click()

    buy_elem = driver.find_element(By.XPATH, "//*[@id='search-page-container']/div[3]/div/div/div[2]/div/div/div[2]/section/article[1]/div/div/div[3]/div[2]/div[2]/button")
    buy_elem.click()
    time.sleep(2)

    # looking for the button 'Перейти до кошика' and emulate the click with the left mouse
    btn_elem = driver.find_element(By.XPATH, "//*[@id='cart-preview']/div/div[2]/div[2]/button[1]")
    btn_elem.click()

    # looking for the button 'оформити замовлення' and emulate the click with the left mouse
    btn_elem = driver.find_element(By.XPATH, "//*[@id='desktop-promocode-container']/div/div[2]/div[1]")
    btn_elem.click()

    # looking for the field 'місто доставки' and enter the text
    field = driver.find_element(By.XPATH, "//*[@id='select2-select-city-first-container']")
    field.click()
    time.sleep(2)
    field = driver.find_element(By.XPATH, " //input[@type='search']")
    field.send_keys("Самар")
    time.sleep(3)

    # Choose from the city list 'Самар, Дніпропетровська обл.' and emulate the click with the left mouse
    city_elem = driver.find_element(By.XPATH, "//*[@id='select2-select-city-first-results']/li[2]")
    city_elem.click()

    # looking for the field 'ваш телефон' and enter the phone number
    field = driver.find_element(By.XPATH, "//*[@id='Phone']")
    field.send_keys("0631234567")

    # looking for the field 'Ім'я' and enter the name
    field = driver.find_element(By.ID, "Name")
    field.send_keys("Володимир")

    # looking for the field 'Прізвище' and enter the last name
    field = driver.find_element(By.ID, "LastName")
    field.send_keys("Черненко")

    # looking for the field 'По батькові' and enter the patronymic
    field = driver.find_element(By.ID, "MiddleName")
    field.send_keys("Васильович")

    # looking for the button 'Продовжити Оформлення' of form '1.Ваші контактні дані' and emulate the click with the left mouse
    btn_elem = driver.find_element(By.XPATH,"//*[@id='contacts-block']/div[2]/div[2]/div[2]/div/button")
    btn_elem.click()
    time.sleep(2)

    # Check data from form'1.Ваші контактні дані'
    name = driver.find_element(By.ID, "customer-name").text
    assert name == "Володимир"
    lastname = driver.find_element(By.ID, "customer-surname").text
    assert lastname == "Черненко"
    phone = driver.find_element(By.ID, "customer-phone").text
    assert phone == "+38(063) 1234567"

    # Try to close the banner if it is
    wait = WebDriverWait(driver, 4)
    try:
        cookie_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[16]/div/div[2]/button[1]"))
        )
        cookie_btn.click()
    except Exception:
        pass  # If the banner is not found, continue without an error

    # looking for the element 'Оберіть точку самовивозу' of form '2.Доставка' and emulate the click with the left mouse
    elem = driver.find_element(By.ID, "select2-storeId-container")
    elem.click()
    time.sleep(2)

    # choose from the list the point of self -export 'МАГ ДН Самар, Гетьманська вул., 47А' and emulate the click with the left mouse
    point_elem = driver.find_element(By.ID, "select2-storeId-results")
    point_elem.click()
    
    # looking for the button 'Продовжити Оформлення' of form '2.Доставка' and emulate the click with the left mouse
    btn_elem = driver.find_element(By.XPATH,"//*[@id='delivery-types']/div[2]/div[2]/div[2]/button")
    btn_elem.click()
    time.sleep(2)
    
    # Check data from form '2.Доставка'
    shop_delivery = driver.find_element(By.ID, "selected-delivery-specs-title").text
    assert shop_delivery == "МАГ ДН Самар, Гетьманська вул., 47А"

    # Find element 'Оплата при отриманні' of form '3.Оплата' and emulate the click with the left mouse
    elem = driver.find_element(By.XPATH, "//*[@id='payment-types']/div[2]/div[1]/div[1]/div/div[1]/div/div/label")
    elem.click()    

    # looking for the button 'Продовжити Оформлення' of form '3.Оплата' and emulate the click with the left mouse
    btn_elem = driver.find_element(By.XPATH,"//*[@id='payment-types']/div[2]/div[2]/button")
    btn_elem.click()
    time.sleep(2)

    # Check data from form '3.Оплата'
    payment_info = driver.find_element(By.ID, "payment-title").text 
    assert payment_info == "Оплата при отриманні"

    # Find element 'Я' of form '4.Отримувач' and emulate the click with the left mouse
    elem = driver.find_element(By.XPATH, "//*[@id='recipient-types']/div[2]/div/div[1]/div[1]/label")
    elem.click()
    
    # looking for the button 'Згорнути' of form '4.Отримувач' and emulate the click with the left mouse
    btn_elem = driver.find_element(By.XPATH,"//*[@id='recipient-types']/div[1]/div")
    btn_elem.click()    

    # Check data from form '4.Отримувач'
    recipient_info = driver.find_element(By.XPATH, "//*[@id='checkout-form']/div[4]/div/div[6]/div[2]").text
    assert recipient_info == "Володимир Черненко   +38 (063) 123 45 67"

    driver.close()


