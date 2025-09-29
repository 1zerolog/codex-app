"""Lucky Number mini oyun akışı."""

from __future__ import annotations

import random
from typing import Callable

from .session import WalletSession


def play_lucky_number(
    session: WalletSession,
    *,
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> None:
    """1-10 arası sayı tahmini oyunu."""

    secret = random.randint(1, 10)
    attempts = 3
    output_fn("\nLucky Number oyununa hoş geldiniz! 1 ile 10 arasında bir sayı tuttum.")

    while attempts:
        guess_raw = input_fn(f"Tahmininizi girin ({attempts} deneme kaldı): ")
        if not guess_raw.strip().isdigit():
            output_fn("Lütfen sadece sayı girin.")
            continue
        guess = int(guess_raw)
        if guess < 1 or guess > 10:
            output_fn("Tahmin 1 ile 10 arasında olmalı.")
            continue

        if guess == secret:
            output_fn("Tebrikler! Sayıyı doğru tahmin ettiniz.")
            session.register_win()
            return
        if guess < secret:
            output_fn("Daha büyük bir sayı deneyin.")
        else:
            output_fn("Daha küçük bir sayı deneyin.")
        attempts -= 1

    output_fn(f"Üzgünüm, deneme hakkınız bitti. Doğru sayı {secret} idi.")
    session.register_loss()
