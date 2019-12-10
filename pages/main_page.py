from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.login_page import LoginPage


class MainPage(BasePage):
    def go_to_basket(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_basket_link(self):
        self.is_element_present(*MainPageLocators.LOGIN_LINK)
