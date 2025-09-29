"""Cüzdan girişli Lucky Number mini uygulamasının komut satırı giriş noktası."""

from __future__ import annotations

from mini_app.ui import MainMenu


def main() -> None:
    """CLI menüsünü başlat."""

    menu = MainMenu()
    try:
        menu.run()
    except SystemExit:
        raise
    except KeyboardInterrupt:
        print("\nKlavye kısayolu ile çıkış yapıldı. Görüşmek üzere!")


if __name__ == "__main__":
    main()
