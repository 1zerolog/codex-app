"""Oturum yönetimi ve istatistik modelleri."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class WalletSession:
    """Aktif cüzdan oturumu için durum nesnesi."""

    address: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    games_played: int = 0
    games_won: int = 0

    @property
    def win_rate(self) -> float:
        if self.games_played == 0:
            return 0.0
        return (self.games_won / self.games_played) * 100

    def register_win(self) -> None:
        self.games_played += 1
        self.games_won += 1

    def register_loss(self) -> None:
        self.games_played += 1

    def summary(self) -> str:
        return (
            f"Cüzdan: {self.address}\n"
            f"Oturum açma zamanı: {self.created_at:%Y-%m-%d %H:%M:%S} UTC\n"
            f"Toplam oyun: {self.games_played}\n"
            f"Kazanılan oyun: {self.games_won}\n"
            f"Kazanma oranı: {self.win_rate:.2f}%"
        )
