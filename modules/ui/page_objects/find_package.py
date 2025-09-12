from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class FindBox(BasePage):
    URL = 'https://novaposhta.ua/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(FindBox.URL)

    def find_box(self,number_of_TTN):

        # Знаходимо поле, в яке будемо вводити номер посилки
        field = self.driver.find_element(By.XPATH, "//input[@placeholder='Введіть номер посилки']")

        # Вводимо номер посилки
        field.send_keys(number_of_TTN)

        # Знаходимо кнопку 'Відстежити'
        btn_elem = self.driver.find_element(By.XPATH, "//*[@id='__nuxt']/div/main/div/section/div/div[3]/div/div[2]/button")

        # Емулюємо клік лівою кнопкою мишки
        btn_elem.click()
    
    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    def check_title(self, expected_title):
        return self.driver.title == expected_title

