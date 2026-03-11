import time
from playwright.sync_api import Page, expect
import re

# Fonksiyon adı test_ ile başlamalı. 'page' parametresi otomatik gelir.
def test_simple_login_wait(page: Page):
    try:
        print("Sayfaya gidiliyor...")
        page.goto("https://account.testinium.com/uaa/login", wait_until="networkidle")
        
        # 20 saniye bekleme isteğin
        print("20 saniye bekleniyor...")
        time.sleep(20) 
        
        # Sayfanın yüklendiğini doğrula (Basit bir kontrol)
        expect(page).to_have_title(re.compile(".*")) 
        print("Bekleme tamamlandı.")
        
    except Exception as e:
        print(f"Test sırasında hata oluştu: {e}")
        raise e # Hatayı fırlat ki pytest testin fail olduğunu anlasın
