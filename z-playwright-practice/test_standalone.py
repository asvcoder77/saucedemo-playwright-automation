import json
import time

from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/")
    title = page.evaluate("document.title")
    print(title)
    title_new = page.title()
    signup_button = page.locator("(//a[contains(text(),'Sign Up')])[2]")
    signup_button.click(button="right")
    signup_button.press("Control+C")

    time.sleep(1)
    browser.close()


def test_login(page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.locator("#userEmail").fill("asvishnukaruvannur7@gmail.com")
    page.locator("#userPassword").fill("Vi@12345")
    page.locator("#login").click()
    page.locator(
        "//b[contains(text(),'ADIDAS ORIGINAL')]/parent::h5/following-sibling::button[contains(text(),'Add To Cart')]"
    ).click()



def login_bypassed(page: Page):
    login_response = page.request.post("https://rahulshettyacademy.com/api/ecom/auth/login", data={
        "userEmail": "asvishnukaruvannur7@gmail.com",
        "userPassword": "Vi@12345"}, )
    assert login_response.ok, login_response.text()
    token = login_response.json()["token"]
    page.add_init_script(f"localStorage.setItem('token', {json.dumps(token)})")
    page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")
    assert page.url.endswith("/dashboard/dash")

def test_screenshot(page: Page):
    login_bypassed(page)
    page.locator('img.card-img-top').nth(2).screenshot(path='../ss.png')
    page.screenshot(path='../ss2.png', full_page=True)
    page.screenshot(path='../ss3.png')

