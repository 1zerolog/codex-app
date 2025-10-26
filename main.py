"""Basit cüzdan girişli mini oyun uygulaması."""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass


def is_valid_wallet_address(address: str) -> bool:
    """Basit bir cüzdan adresi doğrulaması yap."""
    address = address.strip()
    if len(address) != 42 or not address.startswith("0x"):
        return False
    try:
        int(address[2:], 16)
    except ValueError:
        return False
    return True


@dataclass
class WalletSession:
    address: str
    games_played: int = 0
    games_won: int = 0

    @property
    def win_rate(self) -> float:
        if self.games_played == 0:
            return 0.0
        return self.games_won / self.games_played * 100


def prompt_wallet_login() -> WalletSession | None:
    """Cüzdan adresi iste ve doğrula."""
    print("\nCüzdan girişine hoş geldiniz. Çıkmak için 'q' yazın.")
    while True:
        address = input("Cüzdan adresinizi girin: ")
        if address.lower() == "q":
            return None
        if is_valid_wallet_address(address):
            print(f"Cüzdan doğrulandı: {address}")
            return WalletSession(address=address)
        print("Geçersiz cüzdan adresi. Lütfen tekrar deneyin (örn. 0x ile başlayan 42 karakter).")


def play_lucky_number(session: WalletSession) -> None:
    """1-10 arasında rastgele sayı tahmin oyunu."""
    secret = random.randint(1, 10)
    attempts = 3
    print("\nLucky Number oyununa hoş geldiniz! 1 ile 10 arasında bir sayı tuttum.")
    for remaining in range(attempts, 0, -1):
        guess_raw = input(f"Tahmininizi girin ({remaining} deneme kaldı): ")
        if not guess_raw.isdigit():
            print("Lütfen sadece sayı girin.")
            continue
        guess = int(guess_raw)
        if guess < 1 or guess > 10:
            print("Tahmin 1 ile 10 arasında olmalı.")
            continue

        if guess == secret:
            print("Tebrikler! Sayıyı doğru tahmin ettiniz.")
            session.games_played += 1
            session.games_won += 1
            print("Oyun sona erdi! Menüye dönülüyor.")
            return
        if guess < secret:
            print("Daha büyük bir sayı deneyin.")
        else:
            print("Daha küçük bir sayı deneyin.")
    else:
        session.games_played += 1
        print(f"Üzgünüm, deneme hakkınız bitti. Doğru sayı {secret} idi.")
        print("Oyun sona erdi! Menüye dönülüyor.")


def show_stats(session: WalletSession) -> None:
    print("\n--- Oyun İstatistikleri ---")
    print(f"Cüzdan: {session.address}")
    print(f"Toplam oyun: {session.games_played}")
    print(f"Kazandığı oyun: {session.games_won}")
    print(f"Kazanma oranı: {session.win_rate:.2f}%")


def main() -> None:
    print("Codex mini oyun uygulamasına hoş geldiniz!")
    session: WalletSession | None = None

    while True:
        if session is None:
            print("\n--- Ana Menü ---")
            print("1) Cüzdan ile giriş yap")
            print("2) Çıkış")
            choice = input("Seçiminiz: ")

            if choice == "1":
                session = prompt_wallet_login()
            elif choice == "2":
                print("Görüşmek üzere!")
                sys.exit(0)
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
        else:
            print("\n--- Oyun Menüsü ---")
            print("1) Lucky Number oyna")
            print("2) İstatistikleri görüntüle")
            print("3) Oturumu kapat")
            print("4) Çıkış")
            choice = input("Seçiminiz: ")

            if choice == "1":
                play_lucky_number(session)
            elif choice == "2":
                show_stats(session)
            elif choice == "3":
                print("Oturum kapatıldı.")
                session = None
            elif choice == "4":
                print("Görüşmek üzere!")
                sys.exit(0)
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()
