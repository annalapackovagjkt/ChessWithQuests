from typing import Tuple
from model.figurka import Figurka, Vektor


class Kůň(Figurka):
    def __init__(self, barva_tym: int, pozice: Tuple[int, int] = (0, 0)):
        super().__init__("Kůň", barva_tym, pozice, skok=True)
        l_vektory = [
            Vektor(1, 2), Vektor(2, 1), Vektor(2, -1), Vektor(1, -2),
            Vektor(-1, -2), Vektor(-2, -1), Vektor(-2, 1), Vektor(-1, 2)
        ]
        self.vektory = l_vektory
        self.vektory_utoku = l_vektory