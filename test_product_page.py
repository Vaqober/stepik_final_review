from pages.product_page import ProductPage
from pages.product_page import ProductPageLocators
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import time


"""@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])"""


def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_success_message()


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
