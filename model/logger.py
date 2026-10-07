from typing import List, Any, Dict

class GameLogger:

    def __init__(self, soubor_path: str = "game.log"):
        self.soubor_path: str = soubor_path
        self.vytvor_soubor(soubor_path)

    def vytvor_soubor(self, filename: str) -> None:
        self.soubor_path = filename
        with open(self.soubor_path, "a", encoding="utf-8") as f:
            f.write("--- NOVÁ HRA ZAHÁJENA ---\n")

    def uloz_tah(self, tah: Any) -> None:
        with open(self.soubor_path, "a", encoding="utf-8") as f:
            f.write(f"Tah: {tah}\n")

    def souradnice_na_notaci(pozice: tuple[int, int]) -> str:
        """Převede (x, y) např. (4, 1) na šachovou notaci 'e2'."""
        sloupce = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        x, y = pozice
        return f"{sloupce[x]}{y + 1}"