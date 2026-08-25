from playwright.sync_api import expect

from pages.checkout_page import CheckoutPage


class CartPage:

    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page):
        self.page = page
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def verify_page_is_open(self):
        expect(self.page).to_have_url(self.URL)

    def checkout(self):
        self.checkout_button.click()
        return CheckoutPage(self.page)



