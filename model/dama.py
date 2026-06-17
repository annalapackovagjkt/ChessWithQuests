from typing import Tuple
from model.figurka import Figurka, Vektor


class Dáma(Figurka):
    def __init__(self, barva_tym: int, pozice: Tuple[int, int] = (0, 0)):
        super().__init__("Dáma", barva_tym, pozice, skok=False)
        dama_vektory = [
            Vektor(0, 1), Vektor(1, 0), Vektor(0, -1), Vektor(-1, 0),
            Vektor(1, 1), Vektor(1, -1), Vektor(-1, -1), Vektor(-1, 1)
        ]
        self.vektory = dama_vektory
        self.vektory_utoku = dama_vektory