from pytest_playwright.pytest_playwright import page
from playwright.sync_api import expect

class CheckoutPage:
    INFORMATION_URL = "https://www.saucedemo.com/checkout-step-one.html"
    OVERVIEW_URL = "https://www.saucedemo.com/checkout-step-two.html"

    def __init__(self, page):
        self.page = page
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.postal_code = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.finish_button = page.get_by_role("button", name="Finish")
        self.order_confirmation = page.get_by_text(
            "Thank you for your order!"
        )

    def verify_information_page_is_open(self):
        expect(self.page).to_have_url(self.INFORMATION_URL)

    def enter_customer_details(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def verify_overview_page_is_open(self):
        expect(self.page).to_have_url(self.OVERVIEW_URL)

    def finish_order(self):
        self.finish_button.click()

    def verify_order_is_complete(self):
        expect(self.order_confirmation).to_be_visible()
