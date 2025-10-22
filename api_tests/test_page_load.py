import time
from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()

#     start_time = time.time()
#     page.goto("https://www.myntra.com", wait_until="domcontentloaded")  # 'load' waits for full load event
#     end_time = time.time()

#     print(f"Page load time: {end_time - start_time:.2f} seconds")

#     browser.close()

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.myntra.com")

    # Get browser performance timing data
    perf_timing = page.evaluate("JSON.stringify(window.performance.timing)")
    import json
    timing = json.loads(perf_timing)

    load_time = timing["loadEventEnd"] - timing["navigationStart"]
    dom_content_loaded = timing["domContentLoadedEventEnd"] - timing["navigationStart"]

    print(f"Total Load Time: {load_time/1000:.2f} s")
    print(f"DOM Content Loaded: {dom_content_loaded/1000:.2f} s")

    browser.close()



def test_myntra_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        start = time.time()
        page.goto("https://www.myntra.com", wait_until="load")
        end = time.time()

        print(f"Page load time: {end - start:.2f}s")
        browser.close()