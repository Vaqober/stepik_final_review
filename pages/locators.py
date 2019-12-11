from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_SUBMIT = (By.XPATH, "//button[@name='registration_submit']")
    LOGIN_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/profile/"


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//div[contains(@class, 'basket-mini')]//a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators():
    PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    PRODUCT_FORM = (By.XPATH, "//article[contains(@class, 'product_page')]")
    ADD_BUTTON_XPATH = (By.XPATH, "//button[@class = 'btn btn-lg btn-primary btn-add-to-basket']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success')]")


class BasketPageLocators():
    ITEM_LINK = (By.XPATH, "//div[contains(@class, 'basket-items')]")
    EMPTY_MESSAGE = (By.XPATH, "//div[contains(@id, 'messages')]//div[contains(@id, 'content')]")

