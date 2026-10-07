from typing import List, Dict, Any


class Quest:

    def __init__(self, id_quest: int, nazev: str, popis: str, odmena: int = 100):
        self.id_quest = id_quest
        self.nazev = nazev
        self.popis = popis
        self.odmena = odmena
        self.splneno: bool = False

    def vyhodnot(self, herni_data: Dict[str, Any]) -> bool:
        return self.splneno
