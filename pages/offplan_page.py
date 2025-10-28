from selenium.webdriver.common.by import By
from pages.base_page import Page

class OffPlanPage(Page):
    OFF_PLAN_BUTTON=(By.XPATH, "//div[contains(text(),'Off-plan') and contains(@class,'g-menu-text')]")

    def click_off_plan(self):
        element = self.wait_until_element_is_present(*self.OFF_PLAN_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
