from view.hlavni_okno import HlavniOknoFrame
from model.manager import GameManager


class GameController:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess with Quests")

        self.game_manager = GameManager()
        self.view = HlavniOknoFrame(self.root, self.game_manager)
        self.view.pack(fill="both", expand=True)

        self.vybrane_policko = None
        self.hra_bezi = True

        self.view.board_view.bind("<Button-1>", self.on_board_click)

    def on_board_click(self, event):
        if not self.hra_bezi:
            return

        velikost = self.view.board_view.velikost_pole
        x = event.x // velikost
        y = event.y // velikost

        if not (0 <= x < 8 and 0 <= y < 8):
            return

        if self.vybrane_policko is None:
            figurka = self.game_manager.plocha.get_figurka(x, y)
            aktualni_hrac = getattr(self.game_manager, "na_tahu", 1)

            if figurka and figurka.barva_tym == aktualni_hrac:
                self.vybrane_policko = (x, y)
                self.view.board_view.vybrane_policko = (x, y)
                self.view.board_view.prekresli()

        else:
            start_x, start_y = self.vybrane_policko

            if (x, y) == (start_x, start_y):
                self.zrus_vyber()
                return

            cilova_figurka = self.game_manager.plocha.get_figurka(x, y)
            aktualni_hrac = getattr(self.game_manager, "na_tahu", 1)
            if cilova_figurka and cilova_figurka.barva_tym == aktualni_hrac:
                self.vybrane_policko = (x, y)
                self.view.board_view.vybrane_policko = (x, y)
                self.view.board_view.prekresli()
                return

            uspech = self.proved_tah_v_modelu(start_x, start_y, x, y)

            if uspech:
                self.zrus_vyber()
                self.view.aktualizuj_vse()
                self.zkontroluj_konec_hry()
            else:
                self.view.info_panel.aktualizuj_stav("Neplatný tah! Zkus to znovu.")

    def zrus_vyber(self):
        self.vybrane_policko = None
        self.view.board_view.vybrane_policko = None
        self.view.board_view.prekresli()

    def proved_tah_v_modelu(self, x1, y1, x2, y2) -> bool:
        if hasattr(self.game_manager, "proved_tah"):
            return self.game_manager.proved_tah(x1, y1, x2, y2)
        elif hasattr(self.game_manager, "tah"):
            return self.game_manager.tah(x1, y1, x2, y2)

        figurka = self.game_manager.plocha.get_figurka(x1, y1)
        if figurka:
            self.game_manager.plocha.nastav_figurku(x2, y2, figurka)
            self.game_manager.plocha.nastav_figurku(x1, y1, None)
            if hasattr(self.game_manager, "na_tahu"):
                self.game_manager.na_tahu *= -1
            return True
        return False

    def zkontroluj_konec_hry(self):
        if getattr(self.game_manager, "konec_hry", False):
            self.hra_bezi = False
            vitez = getattr(self.game_manager, "vitez", "Neznámý")
            self.view.zobraz_konec_hry(f"Hra skončila! Vítěz: {vitez}")

if __name__ == "__main__":
    from tkinter import Tk

    root = Tk()
    controller = GameController(root)
    root.mainloop()