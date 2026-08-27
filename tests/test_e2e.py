import pytest
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@pytest.mark.e2e
def test_end2end(page, credentials, customer_details):

    login_page = LoginPage(page)

    login_page.open()
    products_page = login_page.login(credentials["username"],
          credentials["password"])

    products_page.verify_products_page_is_open()
    products_page.add_product("Sauce Labs Onesie")
    cart_page = products_page.open_cart()

    cart_page.verify_page_is_open()
    checkout_page = cart_page.checkout()

    checkout_page.verify_information_page_is_open()
    checkout_page.enter_customer_details(customer_details["first_name"],
          customer_details["last_name"],
          customer_details["postal_code"],)
    checkout_page.continue_checkout()
    checkout_page.verify_overview_page_is_open()
    checkout_page.finish_order()
    checkout_page.verify_order_is_complete()



