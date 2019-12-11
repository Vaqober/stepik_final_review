from pages.product_page import ProductPage
from pages.product_page import ProductPageLocators
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import pytest
import time


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = ProductPageLocators.PRODUCT_LINK
        product_page = ProductPage(browser, link)
        product_page.should_be_login_link()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.should_be_inputs()
        email = str(time.time()) + "@fakemail.org"
        password = "test_password123456"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
        yield

    def test_user_can_add_product_to_basket(self, browser):
        link = ProductPageLocators.PRODUCT_LINK
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_product_page()
        product_page.add_to_basket()
        product_page.should_be_success_message()

    def test_user_cant_see_success_message(self, browser):
        link = ProductPageLocators.PRODUCT_LINK
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_LINK
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = ProductPageLocators.PRODUCT_LINK
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = ProductPageLocators.PRODUCT_LINK
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_LINK
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.should_be_login_link()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_LINK
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_basket_link()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_item()
    basket_page.should_be_basket_message()
