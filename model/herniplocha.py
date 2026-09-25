from typing import List, Optional, Tuple
from model.figurka import Figurka
from model.pesak import Pěšák
from model.vez import Věž
from model.kun import Kůň
from model.strelec import Střelec
from model.dama import Dáma
from model.kral import Král

class HerniPlocha:
    def __init__(self):
        self.mrizka: List[List[Optional[Figurka]]] = [[None for _ in range(8)] for _ in range(8)]
        self.priprav_desku()

    def je_v_mezich(self, x: int, y: int) -> bool:
        return 0 <= x < 8 and 0 <= y < 8

    def get_figurka(self, x: int, y: int) -> Optional[Figurka]:
        if self.je_v_mezich(x, y):
            return self.mrizka[y][x]
        return None

    def poloz_figurku(self, figurka: Figurka, x: int, y: int) -> None:
        if self.je_v_mezich(x, y):
            self.mrizka[y][x] = figurka
            figurka.posun_figurky((x, y))

    def posun_figurku(self, stara_pos: Tuple[int, int], nova_pos: Tuple[int, int]) -> bool:
        sx, sy = stara_pos
        nx, ny = nova_pos

        figurka = self.get_figurka(sx, sy)
        if figurka is None or not self.je_v_mezich(nx, ny):
            return False

        self.mrizka[sy][sx] = None
        self.mrizka[ny][nx] = figurka
        figurka.posun_figurky((nx, ny))
        return True

    def priprav_desku(self) -> None:
        self.mrizka = [[None for _ in range(8)] for _ in range(8)]

        for x in range(8):
            self.poloz_figurku(Pěšák(barva_tym=1), x, 1)

        bily_prvni_rada = [Věž, Kůň, Střelec, Dáma, Král, Střelec, Kůň, Věž]
        for x, cls in enumerate(bily_prvni_rada):
            self.poloz_figurku(cls(barva_tym=1), x, 0)

        for x in range(8):
            self.poloz_figurku(Pěšák(barva_tym=-1), x, 6)

        cerny_prvni_rada = [Věž, Kůň, Střelec, Dáma, Král, Střelec, Kůň, Věž]
        for x, cls in enumerate(cerny_prvni_rada):
            self.poloz_figurku(cls(barva_tym=-1), x, 7)

class Tah:
    def __init__(self, vychozi_pozice, cilova_pozice, figurka, typ_tahu):
        self.vychozi_pozice = vychozi_pozice
        self.cilova_pozice = cilova_pozice
        self.figurka = figurka
        self.typ_tahu = typ_tahu
    def over_platnost(self):
        return True
    def proved_tah(self):
        pass