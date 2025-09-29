# Codex Mini Oyun Uygulaması

Bu depo, cüzdan adresi doğrulamasıyla korunan basit bir Lucky Number mini oyununu içerir. Kullanıcılar geçerli bir Ethereum benzeri cüzdan adresiyle giriş yaptıktan sonra oyunu oynayabilir ve oturum istatistiklerini görüntüleyebilir.

## Özellikler
- Komut satırı tabanlı giriş ve oyun menüleri
- 0x ile başlayan 42 karakterlik cüzdan adresi doğrulaması
- Kazanılan/kaybedilen oyun istatistikleri ve kazanma oranı takibi
- Modüler yapı: `mini_app/` paketi altında oturum, cüzdan ve oyun bileşenleri

## Gereksinimler
- Python 3.11+

Ekstra bağımlılık yoktur; standart kütüphane yeterlidir.

## Kurulum ve Çalıştırma
1. Depoyu klonlayın veya dosyaları yerel bilgisayarınıza alın.
2. Python ortamınızı etkinleştirin (varsa sanal ortam kullanın).
3. Uygulamayı şu komutla başlatın:

   ```bash
   python main.py
   ```

4. Açılan menüden cüzdan adresinizi girerek giriş yapın ve oyunu oynayın.

## Yapı
- `main.py`: Uygulama giriş noktası.
- `mini_app/session.py`: Cüzdan oturumu durumu ve istatistikleri.
- `mini_app/wallet.py`: Cüzdan doğrulama ve giriş yardımcıları.
- `mini_app/game.py`: Lucky Number mini oyunu.
- `mini_app/ui.py`: Komut satırı menüleri ve akış kontrolü.

## Test
Kodun sözdizimi olarak geçerli olduğunu kontrol etmek için:

```bash
python -m compileall .
```
