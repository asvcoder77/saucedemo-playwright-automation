from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_end2end(page):

    login_page = LoginPage(page)

    login_page.open()
    products_page = login_page.login("standard_user","secret_sauce")

    products_page.verify_products_page_is_open()
    products_page.add_product("Sauce Labs Onesie")
    cart_page = products_page.open_cart()

    cart_page.verify_page_is_open()
    checkout_page = cart_page.checkout()

    checkout_page.verify_information_page_is_open()
    checkout_page.enter_customer_details("Vishnu","AS","345678")
    checkout_page.continue_checkout()
    checkout_page.verify_overview_page_is_open()
    checkout_page.finish_order()
    checkout_page.verify_order_is_complete()



