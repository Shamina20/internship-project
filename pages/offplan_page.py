from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class OffPlanPage(Page):
    OFF_PLAN_BUTTON=(By.XPATH, "//div[text()='Off-plan' and @class='g-menu-text']")

    def click_off_plan(self):
        self.click(*self.OFF_PLAN_BUTTON)

