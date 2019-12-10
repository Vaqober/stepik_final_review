from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_basket(self):
        link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        link.click()

    def should_be_basket_link(self):
        self.is_element_present(*MainPageLocators.BASKET_LINK)
