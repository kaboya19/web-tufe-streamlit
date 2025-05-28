import requests
from bs4 import BeautifulSoup
import time
import json
import pandas as pd
from urllib.parse import urljoin, urlparse
import re

class HepsiemlakScraper:
    def __init__(self):
        self.base_url = "https://www.hepsiemlak.com"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        })
        # Cookie support ekle
        self.session.cookies.update({
            'language': 'tr',
        })
        
    def get_search_url(self, city="istanbul", district="", property_type="daire", min_price="", max_price="", page=1):
        """Arama URL'si oluştur"""
        if district:
            url = f"{self.base_url}/kiralik-{property_type}/{city}-{district}?page={page}"
        else:
            url = f"{self.base_url}/kiralik-{property_type}/{city}?page={page}"
            
        # Fiyat filtreleri ekle
        params = []
        if min_price:
            params.append(f"minPrice={min_price}")
        if max_price:
            params.append(f"maxPrice={max_price}")
            
        if params:
            url += "&" + "&".join(params)
            
        return url
    
    def scrape_listings(self, city="istanbul", district="", max_pages=5, delay=3):
        """İlanları scrape et"""
        listings = []
        
        # İlk olarak ana sayfayı ziyaret et (cookie ve session için)
        try:
            print("Ana sayfa ziyaret ediliyor...")
            self.session.get(self.base_url, timeout=10)
            time.sleep(2)
        except:
            pass
        
        for page in range(1, max_pages + 1):
            print(f"Sayfa {page} scraping...")
            
            url = self.get_search_url(city=city, district=district, page=page)
            print(f"URL: {url}")
            
            try:
                # Rastgele delay ekle
                time.sleep(delay + (page * 0.5))
                
                response = self.session.get(url, timeout=15)
                
                # 403 hatası durumunda farklı User-Agent dene
                if response.status_code == 403:
                    print("403 hatası, farklı User-Agent deneniyor...")
                    user_agents = [
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
                    ]
                    
                    for ua in user_agents:
                        self.session.headers.update({'User-Agent': ua})
                        time.sleep(3)
                        response = self.session.get(url, timeout=15)
                        if response.status_code != 403:
                            break
                
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # İlan kartlarını bul
                listing_cards = soup.find_all('div', class_='listing-card')
                
                if not listing_cards:
                    # Alternatif selector'lar dene
                    listing_cards = soup.find_all('div', attrs={'data-testid': 'listing-card'})
                    
                if not listing_cards:
                    # Daha genel bir arama
                    listing_cards = soup.find_all('div', class_=re.compile(r'.*listing.*|.*card.*|.*property.*'))
                
                print(f"Sayfa {page}'da {len(listing_cards)} ilan bulundu")
                
                if not listing_cards:
                    print("İlan kartları bulunamadı, sayfa yapısı değişmiş olabilir")
                    # HTML'i debug için kaydet
                    with open(f'debug_page_{page}.html', 'w', encoding='utf-8') as f:
                        f.write(response.text)
                    print(f"Debug için sayfa debug_page_{page}.html olarak kaydedildi")
                    break
                
                page_listings = self.parse_listings(listing_cards)
                listings.extend(page_listings)
                
                print(f"Sayfa {page}: {len(page_listings)} ilan işlendi")
                
            except requests.RequestException as e:
                print(f"Sayfa {page} için HTTP hatası: {e}")
                if "403" in str(e):
                    print("403 hatası - Bot koruması aktif. Daha uzun bekleme süresi deneyin.")
                    time.sleep(10)
                continue
            except Exception as e:
                print(f"Sayfa {page} için genel hata: {e}")
                continue
                
        return listings
    
    def parse_listings(self, listing_cards):
        """İlan kartlarından veri çıkar"""
        listings = []
        
        for card in listing_cards:
            try:
                listing_data = {}
                
                # Başlık
                title_elem = card.find('h3') or card.find('a', class_=re.compile(r'.*title.*'))
                if title_elem:
                    listing_data['title'] = title_elem.get_text(strip=True)
                
                # Fiyat
                price_elem = card.find('span', class_=re.compile(r'.*price.*|.*amount.*')) or \
                           card.find('div', class_=re.compile(r'.*price.*'))
                if price_elem:
                    price_text = price_elem.get_text(strip=True)
                    listing_data['price'] = self.clean_price(price_text)
                
                # Konum
                location_elem = card.find('span', class_=re.compile(r'.*location.*|.*address.*'))
                if location_elem:
                    listing_data['location'] = location_elem.get_text(strip=True)
                
                # Oda sayısı
                room_elem = card.find('span', string=re.compile(r'\d+\+?\d*\s*oda|room'))
                if room_elem:
                    listing_data['rooms'] = room_elem.get_text(strip=True)
                
                # Alan (m²)
                area_elem = card.find('span', string=re.compile(r'\d+\s*m²'))
                if area_elem:
                    listing_data['area'] = area_elem.get_text(strip=True)
                
                # İlan linki
                link_elem = card.find('a', href=True)
                if link_elem:
                    href = link_elem['href']
                    if not href.startswith('http'):
                        href = urljoin(self.base_url, href)
                    listing_data['url'] = href
                
                # Tarih
                date_elem = card.find('span', class_=re.compile(r'.*date.*|.*time.*'))
                if date_elem:
                    listing_data['date'] = date_elem.get_text(strip=True)
                
                if listing_data:  # En az bir veri varsa ekle
                    listings.append(listing_data)
                    
            except Exception as e:
                print(f"İlan parse hatası: {e}")
                continue
                
        return listings
    
    def clean_price(self, price_text):
        """Fiyat metnini temizle"""
        # Sadece rakamları al
        numbers = re.findall(r'\d+', price_text.replace('.', '').replace(',', ''))
        if numbers:
            return int(''.join(numbers))
        return price_text
    
    def save_to_csv(self, listings, filename="hepsiemlak_listings.csv"):
        """Sonuçları CSV'ye kaydet"""
        if listings:
            df = pd.DataFrame(listings)
            df.to_csv(filename, index=False, encoding='utf-8-sig')
            print(f"{len(listings)} ilan {filename} dosyasına kaydedildi")
        else:
            print("Kaydedilecek ilan bulunamadı")
    
    def save_to_json(self, listings, filename="hepsiemlak_listings.json"):
        """Sonuçları JSON'a kaydet"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(listings, f, ensure_ascii=False, indent=2)
        print(f"{len(listings)} ilan {filename} dosyasına kaydedildi")


# Kullanım örneği
if __name__ == "__main__":
    scraper = HepsiemlakScraper()
    
    # İstanbul'dan kiralık daireler
    print("Hepsiemlak'tan kiralık daire ilanları çekiliyor...")
    listings = scraper.scrape_listings(
        city="istanbul",
        district="",  # Tüm İstanbul için boş bırak, belirli ilçe için "kadikoy" gibi yazabilirsin
        max_pages=2,  # İlk 2 sayfa (403 hatası için azalttık)
        delay=5  # İstekler arası 5 saniye bekle (403 hatası için artırdık)
    )
    
    print(f"\nToplam {len(listings)} ilan bulundu")
    
    # İlk 5 ilanı göster
    for i, listing in enumerate(listings[:5], 1):
        print(f"\n{i}. İlan:")
        for key, value in listing.items():
            print(f"  {key}: {value}")
    
    # Dosyalara kaydet
    if listings:
        scraper.save_to_csv(listings)
        scraper.save_to_json(listings)
    else:
        print("\n⚠️  403 hatası devam ediyorsa şu seçenekleri deneyin:")
        print("1. VPN kullanın")
        print("2. delay'i 10 saniyeye çıkarın") 
        print("3. max_pages'i 1'e indirin")
        print("4. Farklı bir site deneyin (sahibinden.com gibi)")
    
    # Özet istatistikler
    if listings:
        prices = [listing.get('price') for listing in listings if isinstance(listing.get('price'), int)]
        if prices:
            print(f"\nFiyat İstatistikleri:")
            print(f"En düşük: {min(prices):,} TL")
            print(f"En yüksek: {max(prices):,} TL")
            print(f"Ortalama: {sum(prices)//len(prices):,} TL")