"""Cüzdan doğrulama ve oturum açma yardımcıları."""

from __future__ import annotations

from typing import Callable, Optional

from .session import WalletSession


def is_valid_wallet_address(address: str) -> bool:
    """Basit format kurallarına göre cüzdan adresini doğrula."""

    normalized = address.strip()
    if len(normalized) != 42 or not normalized.startswith("0x"):
        return False
    try:
        int(normalized[2:], 16)
    except ValueError:
        return False
    return True


def prompt_wallet_login(
    *,
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> Optional[WalletSession]:
    """Kullanıcıdan cüzdan adresi al ve doğrulanırsa oturum oluştur."""

    output_fn("\nCüzdan girişine hoş geldiniz. Çıkmak için 'q' yazın.")
    while True:
        address = input_fn("Cüzdan adresinizi girin: ")
        if address.lower().strip() == "q":
            output_fn("İstek üzerine cüzdan girişi iptal edildi.")
            return None
        if is_valid_wallet_address(address):
            session = WalletSession(address=address.strip())
            output_fn(f"Cüzdan doğrulandı: {session.address}")
            return session
        output_fn("Geçersiz cüzdan adresi. Örnek: 0x ile başlayan 42 karakter.")
