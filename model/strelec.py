from typing import Tuple
from model.figurka import Figurka, Vektor


class Střelec(Figurka):
    def __init__(self, barva_tym: int, pozice: Tuple[int, int] = (0, 0)):
        super().__init__("Střelec", barva_tym, pozice, skok=False)
        strelec_vektory = [Vektor(1, 1), Vektor(1, -1), Vektor(-1, -1), Vektor(-1, 1)]
        self.vektory = strelec_vektory
        self.vektory_utoku = strelec_vektory