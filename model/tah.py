class Tah:
    def __init__(self, vychozi_pozice, cilova_pozice, figurka, typ_tahu):
        self.vychozi_pozice = vychozi_pozice
        self.cilova_pozice = cilova_pozice
        self.figurka = figurka
        self.typ_tahu = typ_tahu
    def over_platnost(self):
        return True
    def proved_tah(self):
        pass

    def __init__(self, odkud: str = "", kam: str = "", figurka: str = ""):
        self.odkud = odkud
        self.kam = kam
        self.figurka = figurka

    def __str__(self):
        return f"{self.figurka} {self.odkud}->{self.kam}".strip()