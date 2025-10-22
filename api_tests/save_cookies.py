import json
from playwright.sync_api import sync_playwright

def save_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com")

        page.fill('[data-test="username"]', "standard_user")
        page.fill('[data-test="password"]', "secret_sauce")
        page.click('[data-test="login-button"]')

        page.wait_for_url("**/inventory.html")

        cookies = context.cookies()


        with open("cookies.json", "w") as f:
            json.dump(cookies, f, indent=4)

        print("Cookies saved to cookies.json")

        browser.close()

if __name__ == "__main__":
    save_cookies()
