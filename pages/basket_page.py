from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_basket_item(self):
        self.is_not_element_present(*BasketPageLocators.ITEM_LINK)

    def should_be_basket_message(self):
        self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE)