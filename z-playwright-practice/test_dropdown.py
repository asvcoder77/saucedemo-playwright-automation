from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,args=["--start-maximied"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    dropdown=page.locator("#dropdown-class-example")

    #select by value
    dropdown.select_option("Option1")
    page.wait_for_timeout(2000)

    #select by label
    dropdown.select_option(label="Option2")
    page.wait_for_timeout(2000)

    #custom dropdown
    page.goto("https://playwrightlab.github.io/index.html")
    element = page.locator("#country")
    element.scroll_into_view_if_needed()
    element.select_option("Germany")
    page.wait_for_timeout(2000)

    #multiselect
    ele= page.locator("#multiSelect")
    ele.scroll_into_view_if_needed()
    ele.select_option("Vue.js")
    page.wait_for_timeout(2000)
    ele.select_option("React")
    page.wait_for_timeout(2000)
    

