from typing import Tuple
from model.figurka import Figurka, Vektor


class Pěšák(Figurka):
    def __init__(self, barva_tym: int, pozice: Tuple[int, int] = (0, 0)):
        super().__init__("Pěšák", barva_tym, pozice, skok=False)
        self.vektory = [Vektor(0, 1 * barva_tym)]
        self.vektory_utoku = [Vektor(1, 1 * barva_tym), Vektor(-1, 1 * barva_tym)]