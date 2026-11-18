from tkinter import Tk, Frame, Canvas, Label
from model.manager import GameManager


class BoardView(Canvas):

    def __init__(self, parent, game_manager, velikost_pole=60):
        self.velikost_pole = velikost_pole
        sirka_vyska = 8 * self.velikost_pole
        super().__init__(parent, width=sirka_vyska, height=sirka_vyska, bg="white")

        self.game_manager = game_manager
        self.vybrane_policko = None

    def prekresli(self):
        self.delete("all")
        self.vykresli_sachovnici()
        self.vykresli_figurky()

    def vykresli_sachovnici(self):
        barvy = ["#f0d9b5", "#b58863"]

        for radek in range(8):
            for sloupec in range(8):
                x1 = sloupec * self.velikost_pole
                y1 = radek * self.velikost_pole
                x2 = x1 + self.velikost_pole
                y2 = y1 + self.velikost_pole

                if self.vybrane_policko == (sloupec, radek):
                    barva = "#baca44"
                else:
                    barva = barvy[(radek + sloupec) % 2]

                self.create_rectangle(
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

                    self.create_text(
                        cx + 1, cy + 1, text=symbol,
                        font=("Arial", 36), fill="#000000"
                    )
                    self.create_text(
                        cx, cy, text=symbol,
                        font=("Arial", 36), fill=barva_textu
                    )


class QuestPanelView(Frame):

    def __init__(self, parent, game_manager):
        super().__init__(parent, bg="#2e2e2e", width=250)
        self.pack_propagate(False)
        self.game_manager = game_manager

        Label(self, text="🎯 Aktivní Quests", font=("Arial", 14, "bold"), fg="white", bg="#2e2e2e").pack(pady=(15, 10))

        self.seznam_frame = Frame(self, bg="#2e2e2e")
        self.seznam_frame.pack(fill="both", expand=True, padx=10)

    def aktualizuj_questy(self):
        for widget in self.seznam_frame.winfo_children():
            widget.destroy()

        questy = getattr(self.game_manager, "questy", None) or getattr(self.game_manager, "quests", [])

        if not questy:
            Label(self.seznam_frame, text="Žádné aktivní questy", font=("Arial", 10), fg="#aaaaaa", bg="#2e2e2e").pack(
                anchor="w")
            return

        for q in questy:
            nazev = getattr(q, "nazev", str(q))
            splneno = getattr(q, "splneno", False)

            barva = "#4caf50" if splneno else "#dddddd"
            prefix = "✔ " if splneno else "• "

            Label(
                self.seznam_frame,
                text=f"{prefix}{nazev}",
                font=("Arial", 11),
                fg=barva,
                bg="#2e2e2e",
                wraplength=230,
                justify="left"
            ).pack(anchor="w", pady=4)

class InfoPanelView(Frame):
    def __init__(self, parent, game_manager):
        super().__init__(parent, bg="#1f1f1f", height=40)
        self.game_manager = game_manager
        self.label_stav = Label(self, text="Na tahu: Bílý", font=("Arial", 12, "bold"), fg="white", bg="#1f1f1f")
        self.label_stav.pack(pady=8)

    def aktualizuj_stav(self, zprava=None):
        if zprava:
            self.label_stav.config(text=zprava)
            return

        hrac = getattr(self.game_manager, "na_tahu", 1)
        text_hrace = "Bílý (♙)" if hrac == 1 else "Černý (♟)"
        self.label_stav.config(text=f"Na tahu: {text_hrace}")

class HlavniOknoFrame(Frame):
    def __init__(self, root: Tk, game_manager) -> None:
        super().__init__(root, bg="#222222")
        self.game_manager = game_manager

        self.info_panel = InfoPanelView(self, self.game_manager)
        self.info_panel.pack(side="top", fill="x")

        obsah = Frame(self, bg="#222222")
        obsah.pack(fill="both", expand=True, padx=10, pady=10)

        self.board_view = BoardView(obsah, self.game_manager, velikost_pole=60)
        self.board_view.pack(side="left", padx=(0, 10))

        self.quest_panel = QuestPanelView(obsah, self.game_manager)
        self.quest_panel.pack(side="right", fill="y")

        self.aktualizuj_vse()

    def aktualizuj_vse(self):
        self.board_view.prekresli()
        self.quest_panel.aktualizuj_questy()
        self.info_panel.aktualizuj_stav()

    def zobraz_konec_hry(self, zprava: str):
        messagebox.showinfo("Konec hry", zprava)

if __name__ == "__main__":
    root = Tk()
    root.title("Chess with Quests")
    game_manager = GameManager()
    view = HlavniOknoFrame(root, game_manager)
    view.pack(fill="both", expand=True)
    root.mainloop()