from playwright.sync_api import sync_playwright
import time, base64

def join_gimkit(code, name):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto("https://www.gimkit.com/join", wait_until="networkidle")

            # DEBUG: show HTML
            print(page.content())

            # DEBUG: screenshot
            page.screenshot(path="debug.png")
            with open("debug.png", "rb") as f:
                print(base64.b64encode(f.read()).decode())

            # DEBUG: list all inputs/buttons
            print("INPUTS:", page.locator("input").all_text_contents())
            print("BUTTONS:", page.locator("button").all_text_contents())

            # WAIT for Cloudflare
            page.wait_for_timeout(5000)

            # Try real selectors
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
