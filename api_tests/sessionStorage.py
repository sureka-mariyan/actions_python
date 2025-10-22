from playwright.sync_api import sync_playwright

def test_session_storage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Visit the target site
        page.goto("https://www.saucedemo.com")

        # ✅ Set a sessionStorage item
        page.evaluate("sessionStorage.setItem('token', 'abc123')")

        # ✅ Get a sessionStorage item
        token = page.evaluate("sessionStorage.getItem('token')")
        print("Session token:", token)

        # ✅ Remove an item
        page.evaluate("sessionStorage.removeItem('token')")

        # ✅ Confirm it's removed
        token_after_removal = page.evaluate("sessionStorage.getItem('token')")
        print("After removal:", token_after_removal)  # Should print: None

        # ✅ Optional: Clear entire sessionStorage
        page.evaluate("sessionStorage.clear()")

        browser.close()

test_session_storage()
