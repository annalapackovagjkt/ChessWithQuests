from typing import Tuple
from model.figurka import Figurka, Vektor


class Pěšák(Figurka):
    def __init__(self, barva_tym: int, pozice: Tuple[int, int] = (0, 0)):
        super().__init__("Pěšák", barva_tym, pozice, skok=False)
        self.vektory = [Vektor(0, 1 * barva_tym)]
        self.vektory_utoku = [Vektor(1, 1 * barva_tym), Vektor(-1, 1 * barva_tym)]

    if figurka.nazev == "Pěšák":
        nx, ny = x_stara + 0, y_stara + (1 * figurka.barva_tym)
        if plocha.je_v_mezich(nx, ny) and plocha.get_figurka(nx, ny) is None:
            platne_tahy.append((nx, ny))

            start_rada = 1 if figurka.barva_tym == 1 else 6
            if y_stara == start_rada:
                nx2, ny2 = x_stara, y_stara + (2 * figurka.barva_tym)
                if plocha.get_figurka(nx2, ny2) is None:
                    platne_tahy.append((nx2, ny2))

        for utok_vektor in figurka.vektory_utoku:
            ux, uy = x_stara + utok_vektor.dx, y_stara + utok_vektor.dy
            if plocha.je_v_mezich(ux, uy):
                cil = plocha.get_figurka(ux, uy)
                if cil is not None and cil.barva_tym != figurka.barva_tym:
                    platne_tahy.append((ux, uy))