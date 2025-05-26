from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.hepsiemlak.com/konyaalti-kiralik-sahibinden")
    page.wait_for_timeout(3000)  # Sayfanın yüklenmesini bekleyin
    content = page.content()
    print(content)
    browser.close()
