from typing import List, Tuple, Optional

class Figurka:

    def __init__(
        self, 
        nazev: str, 
        barva_tym: int, 
        pozice: Tuple[int, int] = (0, 0), 
        skok: bool = False
    ):
        self.nazev: str = nazev
        # Barva/Tým: 1 = bílý, -1 = černý
        self.barva_tym: int = barva_tym
        self.pozice: Tuple[int, int] = pozice
        self.vektory: List[Vektor] = []
        self.vektory_utoku: List[Vektor] = []
        self.skok: bool = skok

    def get_pozice() -> Tuple[int, int]:
        return self.pozice

    def posun_figurky(self, nova_pozice: Tuple[int, int]) -> None:
        self.pozice = nova_pozice

    def __repr__(self):
        barva_str = "Bílý" if self.barva_tym == 1 else "Černý"
        return f"{self.nazev}({barva_str}) na {self.pozice}"

