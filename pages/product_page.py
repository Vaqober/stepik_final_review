from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_product_form()

    def should_be_product_url(self):
        page_url = str(self.browser.current_url)
        assert 'catalogue' in page_url, "incorrect product url"

    def should_be_product_form(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_FORM)