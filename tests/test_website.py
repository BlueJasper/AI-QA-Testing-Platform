from playwright.sync_api import sync_playwright


def test_website():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://example.com")
        print("Website title:", page.title())

        browser.close()


test_website()
