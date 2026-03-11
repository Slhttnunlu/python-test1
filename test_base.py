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
import pytest
from playwright.sync_api import Page, expect

# 1. Mutlaka bir fonksiyon içinde olmalı (test_ ile başlamalı)
# 2. 'page' parametresi otomatik olarak Playwright fixture'ından gelir
def test_testinium_suite(page: Page):
    # Sayfa yükleme süresini biraz artıralım (Docker için güvenli liman)
    page.set_default_timeout(60000) 
    
    print("Ana sayfaya gidiliyor...")
    page.goto("https://suite.testinium.com/", wait_until="networkidle")
    
    # Adımlarını buraya taşı
    page.get_by_role("button", name="Resources").click()
    page.get_by_role("link", name="Blogs").click()
    
    # Locator'ı biraz daha esnek yapalım (Text içeriğine göre)
    page.locator("text=Data-Driven Testing: How It").first.click()
    
    # Hata aldığın yer için bekleme ekleyelim
    device_farm_link = page.get_by_role("link", name="Device Farm")
    device_farm_link.wait_for(state="visible")
    device_farm_link.click()
    
    page.get_by_role("link", name="Home").first.click()
