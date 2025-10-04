import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_amazon():

    # creating object to manage the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # open the page https://www.amazon.com/
    driver.get("https://www.amazon.com/")
    driver.maximize_window()
    
    # looking for the field to enter the product name
    field = driver.find_element(By.ID,"twotabsearchtextbox")

    # Entering the product name
    field.send_keys("crocs mens")

    # Looking for the 'Search' button and clicking it
    btn_elem = driver.find_element(By.ID, "nav-search-submit-text")
    btn_elem.click()
    time.sleep(2)
    
    # looking for the element 'options' and clicking it
    btn = driver.find_element(By.ID,"a-autoid-31-announce")
    btn.click()
    
    # looking for the element 'add to list' and clicking it
    btn = driver.find_element(By.NAME,"submit.add-to-registry.wishlist.unrecognized")
    btn.click()

    # checking the title of the page
    assert driver.title == ""
    
    # closing the browser
    driver.close()
