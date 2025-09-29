"""Komut satırı menüleri ve akış kontrolü."""

from __future__ import annotations

from typing import Callable, Optional

from .game import play_lucky_number
from .session import WalletSession
from .wallet import prompt_wallet_login


class MainMenu:
    """Komut satırı tabanlı ana menü denetleyicisi."""

    def __init__(
        self,
        *,
        input_fn: Callable[[str], str] = input,
        output_fn: Callable[[str], None] = print,
    ) -> None:
        self._input = input_fn
        self._output = output_fn
        self._session: Optional[WalletSession] = None

    def run(self) -> None:
        self._output("Codex mini oyun uygulamasına hoş geldiniz!")
        while True:
            if self._session is None:
                if not self._login_menu():
                    return
            else:
                self._game_menu()

    def _login_menu(self) -> bool:
        self._output("\n--- Giriş Menüsü ---")
        self._output("1) Cüzdan ile giriş yap")
        self._output("2) Çıkış")
        choice = self._input("Seçiminiz: ").strip()

        if choice == "1":
            self._session = prompt_wallet_login(input_fn=self._input, output_fn=self._output)
            return True
        if choice == "2":
            self._output("Görüşmek üzere!")
            return False
        self._output("Geçersiz seçim. Lütfen tekrar deneyin.")
        return True

    def _game_menu(self) -> None:
        assert self._session is not None
        self._output("\n--- Oyun Menüsü ---")
        self._output("1) Lucky Number oyna")
        self._output("2) İstatistikleri görüntüle")
        self._output("3) Oturumu kapat")
        self._output("4) Çıkış")
        choice = self._input("Seçiminiz: ").strip()

        if choice == "1":
            play_lucky_number(self._session, input_fn=self._input, output_fn=self._output)
        elif choice == "2":
            self._output("\n--- Oyun İstatistikleri ---")
            self._output(self._session.summary())
        elif choice == "3":
            self._output("Oturum kapatıldı.")
            self._session = None
        elif choice == "4":
            self._output("Görüşmek üzere!")
            raise SystemExit(0)
        else:
            self._output("Geçersiz seçim. Lütfen tekrar deneyin.")
