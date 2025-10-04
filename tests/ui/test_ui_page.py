import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # creating object to manage the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # open the page https://github.com/login 
    driver.get("https://github.com/login")

    # Find the field where we will enter incorrect username or email address
    login_elem = driver.find_element(By.ID, "login_field")

    # Enter incorrect username or email address
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")    

    # Find the field where we will enter incorrect password
    pass_elem = driver.find_element(By.ID, "password")

    # enter incorrect password
    pass_elem.send_keys("wrong password")
    
    # Find button sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    # Simulate left mouse button click
    btn_elem.click()
    
    # Checking that the page title is as expected
    assert driver.title == "Sign in to GitHub · GitHub"
    
    driver.close()