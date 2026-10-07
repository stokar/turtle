# Kaplumbağayı Yakala

Python `turtle` kütüphanesiyle yazılmış küçük bir oyun. Ekranda rastgele hareket eden kaplumbağaya 30 saniye içinde mouse ile kaç kez tıklayabildiğini sayar.

## Nasıl oynanır?

Süre bitmeden kaplumbağaya olabildiğince çok tıkla. Skor ekranın üstünde yazar. Oyundan çıkmak için **ÇIKIŞ** butonuna bas.

## Kurulum ve çalıştırma

Python 3 ve `tkinter` gerekir. Ubuntu/Debian'da:

```
sudo apt install python3-tk python3-venv
```

Sonra:

```
python3 -m venv .venv
source .venv/bin/activate
python oyun.py
```

Ek bir paket kurmak gerekmez.

## Ayarlar

[oyun.py](oyun.py) dosyasının başındaki değerler değiştirilebilir:

- `SURE`: oyun süresi (saniye)
- `HIZ`: kaplumbağanın hızı, küçültürsen yakalamak kolaylaşır
- `GENISLIK`, `YUKSEKLIK`: pencere boyutu
