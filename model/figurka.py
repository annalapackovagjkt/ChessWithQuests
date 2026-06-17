from typing import List, Tuple, Optional


class Vektor:
    def __init__(self, dx: int, dy: int):
        self.dx: int = dx
        self.dy: int = dy

    def __repr__(self):
        return f"Vektor({self.dx}, {self.dy})"


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


class RevizeTahu:

    def __init__(self, herni_plocha):
        self.herni_plocha = herni_plocha
        self.tah: list = []

    def simulate_move(self, figurka: Figurka, nova_pozice: Tuple[int, int]) -> bool:
        puvodni_pozice = figurka.get_pozice()
        figurka.posun_figurky(nova_pozice)

        vlastni_sach = self.check_sach(figurka.barva_tym)

        figurka.posun_figurky(puvodni_pozice)

        return not vlastni_sach

    def check_sach(self, barva_tym: int) -> bool:
        return False

    def check_mat(self, barva_tym: int) -> bool:
        if not self.check_sach(barva_tym):
            return False
        return False

    def check_pat(self, barva_tym: int) -> bool:
        if self.check_sach(barva_tym):
            return False
        return False

