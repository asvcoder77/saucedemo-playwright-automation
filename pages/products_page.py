from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import page

from pages.cart_page import CartPage


class ProductsPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page):
        self.page = page
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')

    def verify_products_page_is_open(self):
        expect(self.page).to_have_url(self.URL)


    def add_product(self,product_name):
        product_card = self.page.locator(".inventory_item").filter(
            has=self.page.get_by_text(product_name, exact=True))
        product_card.get_by_role("button",name="Add to cart").click()

    def open_cart(self):
        self.cart_link.click()
        return CartPage(self.page)





