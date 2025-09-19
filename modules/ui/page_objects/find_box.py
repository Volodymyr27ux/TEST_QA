from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class FindBox(BasePage):
    URL = 'https://novaposhta.ua/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(FindBox.URL)

    def find_box(self,number_of_TTN):
        
        # looking for the field to enter the parcel number
        field = self.driver.find_element(By.XPATH, "//input[@placeholder='Введіть номер посилки']")

        # Entering the parcel number
        field.send_keys(number_of_TTN)

        # Looking for the 'Track' button
        btn_elem = self.driver.find_element(By.XPATH, "//*[@id='__nuxt']/div/main/div/section/div/div[3]/div/div[2]/button")
        btn_elem.click()
    
    def check_box(self, expected_text):

        # Looking for the description of the goods sent ('Constructor')
        elem = self.driver.find_element(By.XPATH,"//*[@id='__nuxt']/div/main/div/div[3]/div/div/div/div[1]/div[3]/div[2]/div/ul/li[5]/div[2]/p")
        value_elem = elem.text
        return value_elem == expected_text
    
        # Checking the title of the page
    def check_title(self, expected_title):
        return self.driver.title == expected_title

