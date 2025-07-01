# PDF Toplu İndirici

Bu proje, bir web sayfasındaki tüm PDF dosyalarını otomatik olarak indirmenizi sağlar.

## Kullanım

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
2. Scripti çalıştırın:
   ```bash
   python pdf_indir.py
   ```
3. PDF dosyaları, scriptin bulunduğu dizinde `indirilen_pdfler` klasörüne kaydedilecektir.

## Gereksinimler
- Python 3.x
- requests
- beautifulsoup4
- tqdm

## Özelleştirme
Başka bir site veya klasör için `pdf_indir.py` dosyasındaki `URL` ve `KLASOR` değişkenlerini düzenleyebilirsiniz.

---

**Not:** Bu script sadece herkese açık PDF dosyalarını indirir. Erişim kısıtlamalı veya korumalı dosyalar için çalışmayabilir. 