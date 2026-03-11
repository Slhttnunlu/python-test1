# First test basic ----------
# import time
# from playwright.sync_api import Page, expect
# import re

# # Fonksiyon adı test_ ile başlamalı. 'page' parametresi otomatik gelir.
# def test_simple_login_wait(page: Page):
#     try:
#         print("Sayfaya gidiliyor...")
#         page.goto("https://account.testinium.com/uaa/login", wait_until="networkidle")
#         
#         # 20 saniye bekleme isteğin
#         print("20 saniye bekleniyor...")
#         time.sleep(20) 
#         
#         # Sayfanın yüklendiğini doğrula (Basit bir kontrol)
#         expect(page).to_have_title(re.compile(".*")) 
#         print("Bekleme tamamlandı.")
#        
#     except Exception as e:
#         print(f"Test sırasında hata oluştu: {e}")
#         raise e # Hatayı fırlat ki pytest testin fail olduğunu anlasın
# Seccond test basic ----------
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://suite.testinium.com/")
    page.get_by_role("button", name="Resources").click()
    page.get_by_role("link", name="Blogs").click()
    page.locator("a").filter(has_text="Data-Driven Testing: How It").click()
    page.get_by_role("contentinfo").get_by_role("link", name="Contact Us").click()
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Device Farm").click()
    page.get_by_role("link", name="Home").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
