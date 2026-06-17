from typing import Tuple
from model.figurka import Figurka, Vektor


class Věž(Figurka):
    def __init__(self, barva_tym: int, pozice: Tuple[int, int] = (0, 0)):
        super().__init__("Věž", barva_tym, pozice, skok=False)
        vez_vektory = [Vektor(0, 1), Vektor(1, 0), Vektor(0, -1), Vektor(-1, 0)]
        self.vektory = vez_vektory
        self.vektory_utoku = vez_vektory