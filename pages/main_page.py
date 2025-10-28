from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class MainPage(Page):
    LOGIN_EMAIL = (By.ID, 'email-2')
    LOGIN_PASSWORD = (By.ID, 'field')
    LOGIN_BUTTON=(By.XPATH, "//a[@wized='loginButton']")


    def open_main(self):
        self.open_url('https://soft.reelly.io')

    def user_login(self,email,password):
        self.input_text(email,*self.LOGIN_EMAIL)
        self.input_text(password,*self.LOGIN_PASSWORD)
        self.click(*self.LOGIN_BUTTON)


