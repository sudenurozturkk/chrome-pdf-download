"""
Bir web sayfasındaki tüm PDF dosyalarını toplu olarak indiren script.
Kullanım: python pdf_indir.py
PDF'ler, scriptin bulunduğu dizinde 'indirilen_pdfler' klasörüne kaydedilir.
"""
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm

# Hedef site
URL = "https://hsgm.saglik.gov.tr/tr/dokumanlar-6.html"
KLASOR = "indirilen_pdfler"

# Klasör oluştur
os.makedirs(KLASOR, exist_ok=True)

# Siteyi çek
print("Site taranıyor...")
response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

# PDF linklerini bul
pdf_linkleri = set()
for link in soup.find_all("a", href=True):
    href = link["href"]
    if href.lower().endswith(".pdf"):
        tam_link = urljoin(URL, href)
        pdf_linkleri.add(tam_link)

print(f"{len(pdf_linkleri)} adet PDF bulundu. İndiriliyor...")

# PDF'leri indir
for pdf_url in tqdm(pdf_linkleri):
    dosya_adi = os.path.join(KLASOR, pdf_url.split("/")[-1])
    try:
        r = requests.get(pdf_url, stream=True, timeout=30)
        r.raise_for_status()
        with open(dosya_adi, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    except Exception as e:
        print(f"Hata: {pdf_url} -> {e}")

print("Tüm PDF'ler indirildi.") 