from tkinter import Tk, Frame, Canvas
from model.manager import GameManager


class HlavniOknoFrame(Frame):
    def __init__(self, root: HlavniOknoFrame, game_manager: object = None) -> None:
        super().__init__(root)
        self.game_manager = game_manager if game_manager is not None else GameManager()
        self.velikost_pole = 60
        sirka_vyska = 8 * self.velikost_pole
        self.herni_deska = Canvas(
            self,
            width=sirka_vyska,
            height=sirka_vyska,
            bg="white"
        )
        self.herni_deska.pack()
        self.vykresli_sachovnici()
        self.vykresli_figurky()

    def vykresli_sachovnici(self):
        """Vykreslí střídavě světlá a tmavá políčka šachovnice 8x8."""
        barvy = ["#f0d9b5", "#b58863"]

        for radek in range(8):
            for sloupec in range(8):
                x1 = sloupec * self.velikost_pole
                y1 = radek * self.velikost_pole
                x2 = x1 + self.velikost_pole
                y2 = y1 + self.velikost_pole

                barva_index = (radek + sloupec) % 2

                self.herni_deska.create_rectangle(
                    x1, y1, x2, y2,
                    fill=barvy[barva_index],
                    outline=""
                )

    def vykresli_figurky(self):
        symboly = {
            ("Pěšák", 1): "♙", ("Pěšák", -1): "♟",
            ("Věž", 1): "♖", ("Věž", -1): "♜",
            ("Kůň", 1): "♘", ("Kůň", -1): "♞",
            ("Střelec", 1): "♗", ("Střelec", -1): "♝",
            ("Dáma", 1): "♕", ("Dáma", -1): "♛",
            ("Král", 1): "♔", ("Král", -1): "♚"
        }

        for y in range(8):
            for x in range(8):
                figurka = self.game_manager.plocha.get_figurka(x, y)
                if figurka:
                    symbol = symboly.get((figurka.nazev, figurka.barva_tym), "?")

                    cx = x * self.velikost_pole + self.velikost_pole / 2
                    cy = y * self.velikost_pole + self.velikost_pole / 2

                    barva_textu = "#ffffff" if figurka.barva_tym == 1 else "#111111"

                    self.herni_deska.create_text(
                        cx + 1, cy + 1, text=symbol,
                        font=("Arial", 36), fill="#000000"
                    )
                    self.herni_deska.create_text(
                        cx, cy, text=symbol,
                        font=("Arial", 36), fill=barva_textu
                    )


if __name__ == "__main__":
    root = Tk()
    root.title("Chess with Quests")
    view = HlavniOknoFrame(root)
    view.pack()
    root.mainloop()