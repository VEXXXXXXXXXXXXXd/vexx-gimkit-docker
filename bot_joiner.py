from playwright.sync_api import sync_playwright
import time

def join_gimkit(code, name):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto("https://www.gimkit.com/join")

            # Enter game code
            page.fill("input[data-testid='game-code-input']", code)
            page.click("button[data-testid='game-code-submit']")
            time.sleep(1)

            # Enter name
            page.fill("input[data-testid='player-name-input']", name)
            page.click("button[data-testid='player-name-submit']")
            time.sleep(2)

            browser.close()
            return True, "Joined successfully"
    except Exception as e:
        return False, str(e)
