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