from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_valid_login(page):

    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user","secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.get_by_text("Test.allTheThings() T-Shirt (Red)").scroll_into_view_if_needed()
    page.locator("//div[contains(text(),'Test.allTheThings() T-Shirt (Red)')]/ancestor::div/following-sibling::div//button").click()
    page.locator("//a[@data-test='shopping-cart-link']").click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    page.get_by_role("button",name="Checkout").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    page.get_by_placeholder("First Name").fill("Vishnu")
    page.get_by_placeholder("Last Name").fill("AS")
    page.get_by_placeholder("Zip/Postal Code").fill("678787")
    page.get_by_role("button",name="Continue").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    page.get_by_role("button",name="Finish").click()

    expect(page.get_by_text("Thank you for your order!")).to_be_visible()

