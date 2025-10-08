from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DeliveryPage(BasePage):
    URL = 'https://www.delivery-auto.com/uk-ua/Home/Index'

    def __init__(self) -> None:
        super().__init__()
        self.wait = WebDriverWait(self.driver,4)

    def go_to(self):
        self.driver.get(DeliveryPage.URL)

    def find_representative(self, address):

        # looking for the button 'Знайти представництво' and clicking it
        btn_elem = self.driver.find_element(By.XPATH,"//*[@id='scrollup']/main/section[2]/div/div[3]/div[1]/a[3]")
        btn_elem.click()
        
        # looking for the field to enter the address or the name of the representative
        field = self.driver.find_element(By.ID,"representatives-search")

        # entering the address or the name of the representative
        field.send_keys(address)
        
        # selecting the second option from the dropdown list
        elem = self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='ui-id-1']/li[2]")))
        elem.click()

        # looking for the button 'Показати на мапі' and clicking it
        btn_elem = self.driver.find_element(By.ID,"representatives-btn")
        btn_elem.click()

    def check_representative_name(self, expected_name):

        # checking the name of the representative on the map
        elem = self.wait.until(EC.presence_of_element_located((By.ID,"header-container")))
        return elem.text == expected_name

    def order_pickup_delivery(self):

        # looking for the link 'Замовити забір та доставку' and clicking it
        link = self.driver.find_element(By.XPATH,"//*[@id='baloon-container']/div[3]/span/a")
        link.click()
    
        # checking the title of the page
    def check_title(self, expected_title):
        return self.driver.title == expected_title