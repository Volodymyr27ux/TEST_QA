import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_posilka():

    # creating object to manage the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # open the page https://novaposhta.ua/
    driver.get("https://novaposhta.ua/")

    # looking for the field to enter the parcel number
    field = driver.find_element(By.XPATH, "//input[@placeholder='Введіть номер посилки']")    

    # Entering the parcel number
    field.send_keys("59001449954672")

    # Looking for the 'Track' button
    btn_elem = driver.find_element(By.XPATH, "//*[@id='__nuxt']/div/main/div/section/div/div[3]/div/div[2]/button")

    # Emulating a left mouse click
    btn_elem.click()
    time.sleep(3)
    
    # Checking the title of the page
    assert driver.title == "Відстежити посилку"

    # checking the description of the goods sent ('Конструктор')
    elem = driver.find_element(By.XPATH,"//*[@id='__nuxt']/div/main/div/div[3]/div/div/div/div[1]/div[3]/div[2]/div/ul/li[5]/div[2]/p")
    value_elem = elem.text
    assert value_elem == 'Конструктор'
    
    # closing the browser
    driver.close()