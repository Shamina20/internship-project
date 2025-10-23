from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class Verify_Page(Page):
    PRODUCTS=(By.CSS_SELECTOR, "[data-test-id*='project-card']")
    PRODUCT_TITLE =  (By.XPATH, "//h4[contains(@class, 'text-base')]")
    PRODUCT_IMAGE = (By.XPATH, "//img[@alt='Project Image']")

    def verify_page(self):
        self.verify_partial_url(f'find.reelly.io')


    def verify_title_and_visible_picture(self):
        self.wait_until_element_appear(*self.PRODUCTS)
        products = self.find_elements(*self.PRODUCTS)

        assert len(products)>0, "No products found"

        for product in products:
            title = product.find_element(*self.PRODUCT_TITLE).text
            image = product.find_element(*self.PRODUCT_IMAGE)

            # Assertions
            assert title.strip() != "", "Product is missing title"
            assert image.is_displayed(), f"Product image is not visible for '{title}'"

    print("All products have titles and visible images.")

