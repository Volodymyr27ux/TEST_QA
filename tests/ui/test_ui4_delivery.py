import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_delivery():

    # creating object to manage the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # open the page 
    driver.get("https://www.delivery-auto.com/uk-ua/Home/Index")

    # looking for the button "Знайти представництво" and clicking it
    btn_elem = driver.find_element(By.XPATH,"//*[@id='scrollup']/main/section[2]/div/div[3]/div[1]/a[3]")
    btn_elem.click()
        
    # looking for the field 'Швидкий пошук представництва Delivery на карті'
    field = driver.find_element(By.ID,"representatives-search")

    # entering the address of the representative office in the search field
    field.send_keys("вул. Спаська, 16")
    time.sleep(2)
    
    # choosing the second option from the dropdown list
    elem = driver.find_element(By.XPATH,"//*[@id='ui-id-1']/li[2]")
    elem.click()

    # looking for the button 'Знайти' and clicking it
    btn_elem = driver.find_element(By.XPATH,"//*[@id='representatives-btn']")
    btn_elem.click()
    time.sleep(2)

    # checking the name of the found representative office
    elem = driver.find_element(By.XPATH,"//*[@id='header-container']")
    assert elem.text == 'САМАР-1 (НОВОМОСКОВСЬК-1)'

    # looking for the link "Замовити забір/доставку вантажу - "НАТИСНИ ТУТ" або зателефонуй" and clicking it
    link = driver.find_element(By.XPATH,"//*[@id='baloon-container']/div[3]/span/a")
    link.click()    

    # checking the title of the page
    assert driver.title == "Заявка на забирання/доставку вантажу | Delivery Auto"

    # closing the browser
    driver.close()