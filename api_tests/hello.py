from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    client = context.new_cdp_session(page)

    client.send("Performance.enable")

    page.goto("https://amazon.com")

    metrics = client.send("Performance.getMetrics")
    for m in metrics["metrics"]:
        print(f"{m['name']}: {m['value']}")

    client.send("Performance.disable")
    browser.close()
