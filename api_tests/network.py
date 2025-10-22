from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    # Create a context with network conditions
    context = browser.new_context(
        **{
            # "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "viewport": {"width": 1280, "height": 720},
            "bypass_csp": True,
            "base_url": "https://www.myntra.com",
            # Simulate network throttling
            "record_har_path": "network_log.har",  # Optional: save network log
        }
    )
    page = context.new_page()

    # Throttle network manually using route
    def slow_route(route, request):
        time.sleep(2)  # Add artificial delay for each request
        route.continue_()

    page.route("**/*", slow_route)

    start = time.time()
    page.goto("https://www.myntra.com", wait_until="load", timeout=160000)
    end = time.time()

    print(f"Page load time under throttling: {end - start:.2f}s")

    browser.close()
