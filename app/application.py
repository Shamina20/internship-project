from pages.base_page import Page
from pages.main_page import MainPage
from pages.offplan_page import OffPlanPage
from pages.verification_page import Verify_Page

class Application:

    def __init__(self,driver):
        self.driver = driver
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.offplan_page=OffPlanPage(driver)
        self.verification_page=Verify_Page(driver)