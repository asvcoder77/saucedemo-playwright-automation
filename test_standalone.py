import json

from playwright.sync_api import Page


def test_login(page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.locator("#userEmail").fill("asvishnukaruvannur7@gmail.com")
    page.locator("#userPassword").fill("Vi@12345")
    page.locator("#login").click()
    page.locator(
        "//b[contains(text(),'ADIDAS ORIGINAL')]/parent::h5/following-sibling::button[contains(text(),'Add To Cart')]"
    ).click()


def test_login_bypassed(page: Page):
    login_response = page.request.post("https://rahulshettyacademy.com/api/ecom/auth/login", data={
        "userEmail": "asvishnukaruvannur7@gmail.com",
        "userPassword": "Vi@12345"}, )
    assert login_response.ok, login_response.text()
    token = login_response.json()["token"]
    page.add_init_script(f"localStorage.setItem('token', {json.dumps(token)})")
    page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")
    assert page.url.endswith("/dashboard/dash")
