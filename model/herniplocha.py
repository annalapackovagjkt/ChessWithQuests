from figurka import Figurka

class HerniPlocha:
    def __init__(self):
        self.rozmery = (8, 8)
        self.herni_deska = []
        self.vyhozene_figurky_b = []
        self.vyhozene_figurky_c = []

    def vrat_obsah(self, souradnice):
       pass

    def posun_figurku(self, tah):
        pass

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