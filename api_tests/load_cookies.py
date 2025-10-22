import json
from playwright.sync_api import sync_playwright

def load_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Load saved cookies
        with open("cookies.json", "r") as f:
            cookies = json.load(f)
            context.add_cookies(cookies)

        page = context.new_page()

        # Go directly to the inventory page
        page.goto("https://www.saucedemo.com/inventory.html")

        # If cookies worked, you'll be logged in already
        page.wait_for_timeout(2000)
        page.pause();
        assert "inventory" in page.url
        print("Session restored using cookies")

        browser.close()

if __name__ == "__main__":
    load_cookies()
