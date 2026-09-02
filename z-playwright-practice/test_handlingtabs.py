import time
from time import sleep

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,
                                args=["--start-maximized"]
                                )
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/windows")
    with page.expect_popup() as popup:
        page.get_by_text("Click Here").click()
    new_tab = popup.value
    print("main_tab",page.url)
    print("new_tab",new_tab.url)
    new_tab.bring_to_front()


    #multple tabs generated at single click scenario
    old_tabs = context.pages.copy()
    new_tab.goto("https://www.hyrtutorials.com/p/window-handles-practice.html")
    new_tab.locator("#newTabsBtn").click()
    new_tab.wait_for_timeout(2000)

    new_tabs = [tab for tab in context.pages if tab not in old_tabs]

    for index, tab in enumerate(new_tabs, start=1):
        tab.wait_for_load_state("domcontentloaded")
        print(f"New tab {index}: {tab.url}")

        

