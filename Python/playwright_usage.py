from playwright.sync_api import sync_playwright
import time

HEADLESS = False

with sync_playwright() as p:
    browser = p.chromium.launch(headless=HEADLESS) # Runs in background
    page = browser.new_page()
    page.goto("https://playwright.dev/python/docs/intro")
    print(page.title())
    if not HEADLESS:
        time.sleep(5)  # Keep the browser open for 5 seconds to see the page
    browser.close()

if __name__ == "__main__":
    pass