from playwright.sync_api import sync_playwright
import time

def join_gimkit(code, name):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto("https://www.gimkit.com/join")

            # NEW SELECTORS
            page.fill("input[placeholder='Game Code']", code)
            page.click("button:has-text('Join')")
            time.sleep(1)

            page.fill("input[placeholder='Name']", name)
            page.click("button:has-text('Join')")
            time.sleep(2)

            browser.close()
            return True, "Joined successfully"
    except Exception as e:
        return False, str(e)
