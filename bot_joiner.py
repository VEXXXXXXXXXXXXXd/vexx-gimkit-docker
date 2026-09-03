from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import time

def join_gimkit(code, name):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=False,  # IMPORTANT: Cloudflare blocks headless
                args=["--disable-blink-features=AutomationControlled"]
            )
            page = browser.new_page()

            stealth_sync(page)  # BYPASS CLOUDFLARE

            page.goto("https://www.gimkit.com/join", wait_until="networkidle")

            # Wait for real join page
            page.wait_for_selector("input[data-testid='game-code-input']", timeout=60000)

            page.fill("input[data-testid='game-code-input']", code)
            page.click("button[data-testid='game-code-submit']")
            time.sleep(1)

            page.wait_for_selector("input[data-testid='player-name-input']", timeout=60000)

            page.fill("input[data-testid='player-name-input']", name)
            page.click("button[data-testid='player-name-submit']")
            time.sleep(2)

            browser.close()
            return True, "Joined successfully"
    except Exception as e:
        return False, str(e)
